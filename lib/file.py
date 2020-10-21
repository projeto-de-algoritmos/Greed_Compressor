from typing import List

class File:
    
    @staticmethod
    def open_file(path: str, read_mode: str, **kwargs) -> List['str']:
        with open(path, read_mode, **kwargs) as file:
            return file.readlines()
    
    @staticmethod
    def save_file(path: str, file_content: bytes,  **kwargs):
        with open(path, "wb") as f:
            f.write(file_content)
