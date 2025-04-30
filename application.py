from tkinter import *
import threading
from docx import Document

import voice_reader
import file_handler

class Application(Tk):
    def __init__(self):
        super().__init__()

        self.width = int(self.winfo_screenwidth() * 0.8)
        self.height = int(self.winfo_screenheight() * 0.8)

        x_screenframe = int((self.winfo_screenwidth() // 2) - (self.width // 2)) // 2
        y_screenframe = int((self.winfo_screenheight() // 2) - (self.height // 2)) // 2

        self.title("Word Voice Reader")
        self.geometry(f"{self.width}x{self.height}+{x_screenframe}+{y_screenframe}")

        self.nameofpathchosenfile = ""
        self.font = ("Arial", 16)

        self.reader = voice_reader.VoiceReader()

    def frame_history(self) -> None:
        frame = Frame(self, 
                      width = (self.width * 0.3), 
                      height = self.height)

        frame.pack()

    def frame_reader(self) -> None:

        def choose_file() -> None:
            self.nameofpathchosenfile = self.file_handler.get_file_name()
            nameofchosenfile = self.nameofpathchosenfile.split("/")[-1]
            nameofdirectorychosenfile = f"Ổ: {self.nameofpathchosenfile[0 : self.nameofpathchosenfile.rfind("/")]}"

            if (len(nameofchosenfile) > (frame["width"] * 0.8) / self.font[1]):
                button_chosenfile["width"] = int((frame["width"] * 0.8) / self.font[1])

            label_chosendirectory["text"] = nameofdirectorychosenfile
            button_chosenfile["text"] = nameofchosenfile

        frame = Frame(self, 
                      width = (self.width * 0.7), 
                      height = (self.height * 0.4))
        
        label_chosenfile = Label(frame, 
                                text = "File đã chọn: ",
                                font = self.font)
        
        label_chosendirectory = Label(frame, 
                                      text = "", 
                                      font = self.font)
        
        button_chosenfile = Button(frame,
                                   text = "Bạn chưa chọn file nào",
                                   font = self.font,
                                   anchor = "w",
                                   command = choose_file)

        frame.place(x = (self.width * 0.3), y = 0)
        label_chosenfile.place(x = 0, y = 0)
        label_chosendirectory.place(x = len(label_chosenfile["text"]) * 16, y = 0)
        button_chosenfile.place(x = 0, y = 32)

    def frame_settingvoice(self) -> None:
        pass

    def run(self) -> None:
        self.frame_history()
        self.frame_reader()
        self.mainloop()