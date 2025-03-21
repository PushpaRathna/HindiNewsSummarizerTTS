from gtts import gTTS
import os

def generate_tts(text):
    tts = gTTS(text, lang="hi")
    file_path = "output.mp3"
    tts.save(file_path)
    return file_path
