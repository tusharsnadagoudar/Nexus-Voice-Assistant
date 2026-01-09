# Nexus Voice Assistant
A personal desktop assistant I built using Python to control my Windows PC with voice commands.

## What it does
I wanted to automate simple tasks on my laptop without using a mouse or keyboard. This script listens for my voice and executes commands using the Windows OS tools.

## Features
- **Lock System:** I used the `os` module to instantly lock the screen when I say the command.
- **Wake Word:** The bot waits for the keyword "Nexus" before it starts processing, so it isn't always listening.
- **Music & Web:** Can open YouTube, Google, or play music from my local folder.

## Tech Stack
- **Python** (Logic)
- **SpeechRecognition** (To convert voice to text)
- **pyttsx3** (To make the bot speak back)
- **OS Module** (To run Windows commands)

## How to use
1. Install the dependencies:
   ```bash
   pip install speechrecognition pyttsx3 pyaudio
   ```

2. Run the main file:
   ```bash
   python main.py
   ```
