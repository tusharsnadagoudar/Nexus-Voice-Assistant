import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import os 

recognizer = sr.Recognizer() 
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # Convert command to lower case once to avoid repeating .lower()
    command = c.lower()
    
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    
    # os system lock
    elif "lock system" in command:
        speak("Locking the device")
        os.system("rundll32.exe user32.dll,LockWorkStation")


    elif command.startswith("play"):
        try:
            song = command.split(" ")[1]
            link = musiclibrary.music[song]
            webbrowser.open(link)
        except Exception as e:
            speak("Song not found in library")

if __name__ == "__main__":
    speak("Initializing Nexus...")
    while True:
        try:
            with sr.Microphone() as source:
                print("recognizing...")
                
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
            
            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}") # Debug print to see what it heard

            if "nexus" in word.lower():
                speak("Yes")
                with sr.Microphone() as source:
                    print("Nexus Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            # Pass prevents the "Error" text from flooding your terminal
            pass

