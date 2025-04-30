class GetDataError(Exception):
    def __init__(self, message: str):
        super().__init__(f"GetDataError: {message}")