TranscribeAndTranslate
A Python-based tool designed to transcribe audio content into text and translate it into different languages.
---
💡 Why I Built This
I am currently learning French by listening to podcasts, but I found that most of them do not have subtitles or transcripts. I built this tool to generate my own subtitles automatically so I can read along while I listen and improve my language skills.
---
🚀 Features
Transcription: Convert speech from audio and video files into text.

Translation: Translate the transcribed text into target languages.
---
📋 Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.8+: Download Python

FFmpeg: Required for processing audio files.

Windows: winget install ffmpeg or download from ffmpeg.org

macOS: brew install ffmpeg

Linux: sudo apt install ffmpeg
---
🛠️ Installation
1.Clone the repository:

Bash

git clone https://github.com/JesseBui/TranscribeAndTranslate.git
cd TranscribeAndTranslate
2.Initialize Project Folders: Run the setup script to create the required input/output directories.

Windows: Double-click setup.bat

macOS/Linux: chmod +x setup.sh then ./setup.sh

3.Set up Virtual Environment (Recommended):

Bash

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
4.Install Dependencies:

Bash

pip install -r requirements.txt
---
💻Usage
Place your audio/video files in the input folder (created by the setup script).

Run the application:

Bash

python main.py
Check the output folder for your results.
