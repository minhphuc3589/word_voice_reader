from tkinter import filedialog

def save_file_name(path: str, data: str) -> None:
    with open(path, "a+") as file:
        file.write(str)

def get_data(path: str, split_char: str = " ") -> [{}]:

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
        print("get_data err")

def get_file_name() -> str:
    return filedialog.askopenfilename(
        title = "Chọn file cần đọc",
        filetypes = (
            ("Word File", "*.doc *.docx"),
            ("All Files", "*.*")
        )
    )