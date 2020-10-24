from lib.file import File
from bitstring import BitStream, BitArray
from lib.decode import Decode
from typing import List
from lib.utils import Utils
from view.terminal.view_utils import ViewUtils
import os

script_dir = os.path.dirname(__file__) 
rel_path = "../../../examples/"
abs_file_path = os.path.join(script_dir, rel_path)


class DecodeView:
    def __init__(self,):
        super(DecodeView, self).__init__()
        self.view_utils = ViewUtils()
        self.decode = Decode()
        self.decode_handler_options = {
            1: self.decode_file_with_manual_path,
            2: self.return_to_menu,
        }

    def get_decode_handler(self, option: int):
        return self.decode_handler_options[option]()

    def decode_file_with_manual_path(self):
        
        
        file = self.view_utils.get_file(self.get_file_path(), 'rb', 2)
        
        decCont = BitArray()
        for line in file:
            decCont.append(line)

        x = BitStream(decCont)
        char_size = Utils.get_encoded_file_char_size(x)
        decoded_header_2 = self.decode.decode_headers(x, char_size)

        hash_table = {}
        decoded_header_2.generate_hashT(hash_table, "")
        inv_map = {v: k for k, v in hash_table.items()}
        decoded_text = self.decode.decode_text(decCont.bin[x.bitpos:x.len], inv_map)

        encoded_file_path = os.path.join(
            abs_file_path,
            f'{self.view_utils.request_file_name_from_user(type_="descromprimido", folder="examples", extension="txt")}.txt')

        File.save_file(encoded_file_path, file_content=decoded_text, type='wt')

        print("\n Arquivo descomprimido com sucesso. Ele está na pasta examples/ no formato .txt \n")

    def get_file_path(self) -> str:
        file_path = input("Insira o nome do arquivo sem extensão. Ele deve estar na pasta compressed_files/ com a extensão .greed_compressed\n")
        compressed_file_path = os.path.join(script_dir, "../../../compressed_files/")
        return os.path.join(compressed_file_path, f"{file_path}.greed_compressed")