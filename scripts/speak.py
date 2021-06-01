from gtts import gTTS
import os
import playsound
from rich import print


class Speak():
    def __init__(self, language):
        self.language = language
        self.location_voice = os.path.join("data", "voice.mp3")

    def speak(self, text, color):
        tts = gTTS(text=text, lang=self.language)
        filename = os.path.join("data", "voice.mp3")
        tts.save(filename)
        print(f"[bold {color}]{text}[/ bold {color}]")
        playsound.playsound(filename)
        os.remove(filename)


if __name__ == '__main__':
    Speak().speak("Hello There")
