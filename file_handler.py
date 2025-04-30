from tkinter import filedialog

import os.path
from exception.data_exception import *

def is_existed_file(path: str) -> bool:
    return os.path.isfile(path)

def create_file(path: str) -> bool:
    try:
        file = open(path, "x")
        file.close()

        return True
    except:
        print("create_file err")
        return False

def save_file(path: str, data: str) -> bool:
    try:
        with open(path, "a+") as file:
            file.write(str)

        return True

    except:
        print("save_file err")
        return False

def get_data(path: str, split_char: str = " ") -> list:

    opened_file_history = []

    try:
        with open(path, "r") as file:
            text_line = file.read()
            splitted_text_line = text_line.splt(split_char)

            date_time = splitted_text_line[0]
            dir_name = splitted_text_line[1]
            file_name = splitted_text_line[2]

            opened_file_history.append({
                "date_time": date_time,
                "dir_name": dir_name,
                "file_name": file_name
            })

        return opened_file_history

    except:
        raise GetDataError("File didn't exist")
        

def get_file_name() -> str:
    return filedialog.askopenfilename(
        title = "Chọn file cần đọc",
        filetypes = (
            ("Word File", "*.doc *.docx"),
            ("All Files", "*.*")
        )
    )