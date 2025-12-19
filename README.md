TranscribeAndTranslate
A Python-based tool designed to transcribe audio content into text and translate it into different languages.
---
🚀 Features
Transcription: Convert speech from audio and video files into text.

Translation: Translate the transcribed text into target languages.

Cross-Platform Setup: Includes automated setup scripts for both Windows and Unix-based systems (macOS/Linux).

📋 Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.8+: Download Python

FFmpeg: Required for processing audio files.

Windows: winget install ffmpeg or download from ffmpeg.org

macOS: brew install ffmpeg

Linux: sudo apt install ffmpeg

🛠️ Installation
Clone the repository:

Bash

git clone https://github.com/JesseBui/TranscribeAndTranslate.git
cd TranscribeAndTranslate
Run the automated setup script: This script will set up a virtual environment and install the necessary dependencies from requirements.txt.

Windows: Double-click setup.bat or run it from the command line:

DOS

setup.bat
macOS / Linux: Make the script executable and run it:

Bash

chmod +x setup.sh
./setup.sh
💻 Usage
Activate the virtual environment (if the setup script didn't keep it open):

Windows: .venv\Scripts\activate

macOS/Linux: source .venv/bin/activate

Run the application:

Bash

python main.py
Note: If the script requires arguments (like input files or language selection), try running python main.py --help to see the available options.
