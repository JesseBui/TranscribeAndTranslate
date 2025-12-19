from openai import OpenAI
from dotenv import load_dotenv
import os
from pydub import AudioSegment
import shutil
import glob

# color helper
class C:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    PINK = "\033[35m" 

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ========================
# PATH CONFIGURATION
# ========================
current_dir = os.path.dirname(os.path.abspath(__file__))

# input
input_path = os.path.join(current_dir, "audio_files") #../audio_files
input_wav_path = os.path.join(current_dir, "wavFiles") #../wavFiles

# output
output_dir = os.path.join(current_dir, "output") # ../output
output_dir_for_untraslated_vtt = os.path.join(output_dir, "untranslatedVTT") #../output/untranslatedVTT

# cleanup
landfill_dir = os.path.join(current_dir, "landfill") #../landfill

# patterns for glob
search_pattern = os.path.join(input_path , "*.mp3") #../audio_files/*.mp3 

def transcribe():
    files = [f for f in os.listdir(input_path) if f.lower().endswith(".mp3")]

    if not files:
        print(f"{C.YELLOW}No MP3 files found for transcription.{C.RESET}\n")
        return []
    
    total = len(files)

    print(f"{C.YELLOW}Starting transcription ({total} files)...{C.RESET}")
    result = []

    for i, file in enumerate(files, start=1 ):
        vtt_name = os.path.basename(file)
        input_mp3_path= os.path.join(input_path, vtt_name)

        print(f"{C.YELLOW}[{i}/{total}] Transcribing: {vtt_name}{C.RESET}")

        with open(input_mp3_path, "rb") as f:
            vtt_translation = client.audio.transcriptions.create(
                model="whisper-1",
                response_format="vtt",
                file=f,
            )
        
        untraslated_vtt_path = os.path.join(output_dir_for_untraslated_vtt, f"{vtt_name}.vtt")

        with open(untraslated_vtt_path, "w", encoding="utf-8") as fout:
            fout.write(vtt_translation)

        print(f"{C.PINK}    Saved untranslated VTT -> {untraslated_vtt_path}{C.RESET}")

        result.append((vtt_translation,vtt_name))
    
    print(f"{C.GREEN}Transcription finished.{C.RESET}\n")
    return result

def translate(vtt_translation, vtt_name, translated_vtt_dir):
    instructions = (
        f"Translate this WebVTT subtitle file into English.\n"
        "Rules:\n"
        "1) Do NOT change timestamps or cue timing lines.\n"
        "2) Do NOT change the 'WEBVTT' header or any metadata lines.\n"
        "3) Translate only the subtitle text lines.\n"
        "4) Keep line breaks similar.\n"
        "Return ONLY valid WebVTT text."
    )

    response = client.responses.create(
    model="gpt-5.1",
    input=[
        {"role": "system", "content":"You are a professional subtitle translator."},
        {"role": "user", "content": instructions},
        {"role": "user", "content": vtt_translation},
    ],
    reasoning={
        "effort": "none"
    }
    )

    translated_vtt_text = response.output_text

    translated_vtt_path = os.path.join(translated_vtt_dir, f"{vtt_name}.en.vtt")
    with open(translated_vtt_path, "w", encoding= "utf-8") as out:
        out.write(translated_vtt_text)

    print(f"{C.GREEN}    Saved translated VTT -> {translated_vtt_path}{C.RESET}")

#I recommend downloading download wav and then convert into mp3. the limit for transcribing mp3 using whisper is only 25mb
def wav_to_mp3():
    files = [f for f in os.listdir(input_wav_path) if f.lower().endswith(".wav")]

    if not files:
        print(f"{C.YELLOW}No WAV files found. Skipping WAV → MP3 step.{C.RESET}\n")
        return
    
    total = len(files)
    print(f"{C.YELLOW}Converting WAV files to MP3...{C.RESET}")

    for i, filename in enumerate(files, start=1):
        print(f"{C.YELLOW}[{i}/{total}] Converting: {filename}{C.RESET}")
        wav_files = os.path.join(input_wav_path, filename)

        mp3_filename = os.path.splitext(os.path.basename(filename))[0] + ".mp3"
        mp3_file = os.path.join(input_path, mp3_filename)
        AudioSegment.from_file(wav_files).export(mp3_file, format = "mp3")

    print(f"{C.GREEN}WAV to MP3 conversion finished.{C.RESET}\n")

def move_to_landfill(search_pattern, landfill_dir):
    filelist = glob.glob(search_pattern)
    if not filelist:
        print(f"{C.YELLOW}No MP3 files to process.{C.RESET}\n")
        return
    
    for files in filelist:
        filename = os.path.basename(files)
        dest = os.path.join(landfill_dir, filename)
        if os.path.exists(dest):
            print(f"{C.YELLOW}Skipped, Files already exist in landfill.{C.RESET}")
            continue
        shutil.move(files, landfill_dir)
    
    print(f"{C.GREEN}MP3 processing complete.{C.RESET}")

def main():
    translated_vtt_folder_name = input("Translated output folder name: ").strip()
    translated_vtt_dir = os.path.join(output_dir, translated_vtt_folder_name)
    os.makedirs(translated_vtt_dir, exist_ok=True)

    wav_to_mp3()
    transcriptions = transcribe()
    if not transcriptions:
        print(f"{C.YELLOW}No transcription found.{C.RESET}\n")
    else:
        print(f"{C.YELLOW}Starting translation phase...{C.RESET}")
        total = len(transcriptions)


        for i, (vtt_text, vtt_name) in enumerate(transcriptions, start=1):
            print(f"{C.YELLOW}[{i}/{total}] Translating: {vtt_name}{C.RESET}")
            translate(vtt_text, vtt_name, translated_vtt_dir)
        
        print(f"{C.GREEN}Translation phase finished.{C.RESET}\n")
    
    question = input("Do you want to move all the mp3 to landfill? Answer Y/N ").lower()
    if question == "y":
        move_to_landfill(search_pattern,landfill_dir)
    elif question == "n":
        print("Mp3 files was not moved.")
    else:
        print("Y or N dude")

if __name__ == "__main__":
    main()