class File:
    
    @staticmethod
    def open_file(path: str, read_mode: str, **kwargs):
        with open(path, 'r', **kwargs) as file:
            return file
    
