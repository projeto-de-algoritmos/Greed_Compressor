from lib.encode import Encode
from lib.file import File
from bitstring import BitArray, BitStream, Bits
from lib.utils import Utils
from view.terminal.menu import Menu
from typing import List
import os
from pathlib import Path

script_dir = os.path.dirname(__file__) 
rel_path = "../../../compressed_files/"
abs_file_path = os.path.join(script_dir, rel_path)


class EncodeView:
    def __init__(self):
        self.encode = Encode()
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
        
        file = self.get_file(file_path)
        
        encoded_file_content = self.encode_file(file)
        
        encoded_file_path = os.path.join(abs_file_path, f'{self.request_file_name_from_user()}.greed_compressor')

        File.save_file(encoded_file_path, file_content=encoded_file_content.tobytes())

        self.calculate_size_diference(file_path, encoded_file_path)

    def request_file_name_from_user(self) -> str:
        print("\nQual será o nome do arquivo comprimido?")
        print("Obs.: Ele será salvo na pasta compressed_files/ com a extensão \{nome\}.greed_compressor")
        print("Obs 2.: O compressor espera arquivos de texto. Ele funciona bem com txt, docx, etc mas não com pdf's e imagens, por exemplo.")
        print("Obs 3.: O compressor funciona com encode em UTF-X.")
        return input("Nome:: ")

    def encode_example_files(self):
        self.menu.encode.get_decode_example_files()
        option = self.menu.get_option([1,2,3,4])

        if option == 4:
            return self.return_to_menu()
    
        print("Codificando arquivo escolhido...", )

        original_file_path = os.path.join(script_dir, "../../../examples/" + self.example_files[option])

        file = self.get_file(original_file_path)

        encoded_file_content = self.encode_file(file)

        encoded_file_path = os.path.join(abs_file_path, f'{self.request_file_name_from_user()}.greed_compressor')

        File.save_file(encoded_file_path, file_content=encoded_file_content.tobytes())

        self.calculate_size_diference(original_file_path, encoded_file_path)
        
    def get_file(self, file_path: str) -> List[str]:
        try:
            return File.open_file(file_path, 'r', encoding='UTF-8')
        except IOError as error:
            input("Erro ao abrir arquivo. Pressione qualquer tecla", error)
            return self.encode_handler_options[3]()

    def encode_file(self, file: List[str]) -> 'BitArray':
        file_content = ''.join(file)
        binary_file_content = BitStream(Bits(file))
        frequencies = self.encode.get_frequencies(file_content)

        parent = self.encode.get_node_tree(frequencies)

        hash_table = {}

        parent.generate_hashT(hash_table, "")
        x = binary_file_content.read(8)

        encoded_text = self.encode.encode_text(file_content, hash_table)

        char_size = Utils.get_largest_char_size(hash_table)

        encoded_header = BitArray()

        encoded_header = Utils.save_char_size_bits(encoded_header, char_size)

        self.encode.encode_headers(parent, encoded_header, char_size)

        bits = encoded_header.bin + encoded_text
        
        return BitArray('0b' + bits)

    def calculate_size_diference(self, original_file_path: str, encoded_file_path: str) -> None:
        original_file_size = Path(original_file_path).stat().st_size
        encoded_file_size = Path(encoded_file_path).stat().st_size
        print("\nCompressão feita com sucesso!!")
        print("Tamanho do arquivo original::", original_file_size, "bytes")
        print("Tamanho do arquivo comprimido::", encoded_file_size, "bytes")
        print("Diferença de tamanho entre os arquivos::", original_file_size - encoded_file_size)
        print("Porcentagem de compressão::", f"{(encoded_file_size / original_file_size) * 100 }" + "%")