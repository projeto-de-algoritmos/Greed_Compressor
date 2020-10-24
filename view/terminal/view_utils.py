from lib.file import File
from typing import List


class ViewUtils:
    def get_file(self, file_path: str, encode_type: str, callback_error_index: int, **kwargs) -> List[str]:
        try:
            return File.open_file(file_path, encode_type)
        except IOError as error:
            input("Erro ao abrir arquivo. Pressione qualquer tecla", error)
            return self.encode_handler_options[callback_error_index]()
    
    def request_file_name_from_user(self, type_: str, folder: str, extension: str) -> str:
        print(f"\nQual será o nome do arquivo { type_}?")
        print(f"Obs.: Ele será salvo na pasta {folder}/ com a extensão <nome>.{extension}")
        if type_ == "comprimido":
            print("Obs 2.: O compressor espera arquivos de texto. Ele funciona bem com txt, mas não com docx, pdf's e imagens, por exemplo.")
            print("Obs 3.: O compressor funciona com encode em UTF-X.")
        else:
            print("Obs 2.: O descrompressor espera arquivos comprimidos em binário. Geralmente estarão no formato <nome>.greed_compressed")
        return input("Nome:: ")