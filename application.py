from tkinter import *
import threading
from docx import Document

import voice_reader

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello world")
        self.geometry("100x100")
        self.voiceReader = voice_reader.VoiceReader()

    def run(self):
        for voice in self.voiceReader.getListOfVoices():
            print(voice)

        self.mainloop()