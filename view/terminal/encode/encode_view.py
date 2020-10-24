from lib.encode import Encode
from lib.file import File
from bitstring import BitArray, BitStream, Bits
from lib.utils import Utils
from view.terminal.menu import Menu
from view.terminal.view_utils import ViewUtils
from view.commons.encode_commons import EncodeCommons
from typing import List
import os
from pathlib import Path

script_dir = os.path.dirname(__file__) 
rel_path = "../../../compressed_files/"
abs_file_path = os.path.join(script_dir, rel_path)


class EncodeView:
    def __init__(self):
        super(EncodeView, self).__init__()
        self.encode = Encode()
        self.view_utils = ViewUtils()
        self.encode_handler_options = {
            1: self.encode_file_with_manual_path,
            2: self.encode_example_files,
            3: self.return_to_menu
        }
        self.example_files = {
            1: 'text.txt',
            2: 'text_2.txt',
            3: 'text_3.txt',
        }

    def get_encode_handler(self, option):
        return self.encode_handler_options[option]()

    def encode_file_with_manual_path(self):
        file_path = input("Insira o caminho do arquivo com extensão\nEx: /home/user/Documentos/Greed_Compressor/examples/text.txt\n")
        
        file = self.view_utils.get_file(file_path, 'r', 3)
        
        encoded_file_content = EncodeCommons.encode_file(file)
        
        encoded_file_path = os.path.join(
            abs_file_path, 
            f'{self.view_utils.request_file_name_from_user(type_="comprimido", folder="compressed_files", extension="greed_compressed")}.greed_compressed')

        File.save_file(encoded_file_path, file_content=encoded_file_content.tobytes())

        self.calculate_size_diference(file_path, encoded_file_path)

    def encode_example_files(self):
        self.menu.encode.get_decode_example_files()
        option = self.menu.get_option([1,2,3,4])

        if option == 4:
            return self.return_to_menu()
    
        print("Codificando arquivo escolhido...", )

        original_file_path = os.path.join(script_dir, "../../../examples/" + self.example_files[option])

        file = self.view_utils.get_file(original_file_path, 'r', 3)

        encoded_file_content = EncodeCommons.encode_file(file)

        encoded_file_path = os.path.join(
            abs_file_path, 
            f'{self.view_utils.request_file_name_from_user(type_="comprimido", folder="compressed_files", extension="greed_compressed")}.greed_compressed')

        File.save_file(encoded_file_path, file_content=encoded_file_content.tobytes())

        self.calculate_size_diference(original_file_path, encoded_file_path)


    def calculate_size_diference(self, original_file_path: str, encoded_file_path: str) -> None:
        original_file_size = Path(original_file_path).stat().st_size
        encoded_file_size = Path(encoded_file_path).stat().st_size
        print("\nCompressão feita com sucesso!!")
        print("Tamanho do arquivo original::", original_file_size, "bytes")
        print("Tamanho do arquivo comprimido::", encoded_file_size, "bytes")
        print("Diferença de tamanho entre os arquivos::", original_file_size - encoded_file_size)
        print("Porcentagem de compressão::", f"{ (1 - (encoded_file_size / original_file_size)) * 100 }" + "%")