from tkinter import filedialog


def save_file_name(path: str, data: str):
    with open("history/history.txt", "a+") as file:
        file.write()

def get_data(path: str):
    pass

def get_file_name() -> str:
    return filedialog.askopenfilename(
        title = "Chọn file cần đọc",
        filetypes = (
            ("Word File", "*.doc *.docx"),
            ("All Files", "*.*")
        )
    )