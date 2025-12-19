# TranscribeAndTranslate

A Python-based tool designed to transcribe audio content into text and translate it into different languages.

## 💡 Why I Built This

I am currently learning French by listening to podcasts, but I found that most of them do not have subtitles or transcripts. I built this tool to generate my own subtitles automatically so I can read along while I listen and improve my language skills.

## 🚀 Features

* **Transcription:** Convert speech from audio and video files into text.
* **Translation:** Translate the transcribed text into target languages.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
* **FFmpeg**: Required for processing audio files.
    * **Windows:** `winget install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/download.html)
    * **macOS:** `brew install ffmpeg`
    * **Linux:** `sudo apt install ffmpeg`

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/JesseBui/TranscribeAndTranslate.git](https://github.com/JesseBui/TranscribeAndTranslate.git)
    cd TranscribeAndTranslate
    ```

2.  **Initialize Project Folders:**
    Run the setup script to create the required `input` and `output` directories.
    * **Windows:** Double-click `setup.bat`
    * **macOS/Linux:**
        ```bash
        chmod +x setup.sh
        ./setup.sh
        ```

3.  **Set up Virtual Environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

1.  Place your audio/video files (e.g., mp3, mp4, wav) in the **input** folder (created by the setup script).
2.  Run the application:
    ```bash
    python main.py
    ```
3.  Check the **output** folder for your generated transcripts and translations.
