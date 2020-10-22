from typing import List
import os

class Menu:
    def __init__(self):
        self.encode = Menu.Encode()
        self.decode = Menu.Decode()
    
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_header(self) -> None:
        self.clear_terminal()
        os.system("pyfiglet Greed Compressor")
        print("======================================")
        print("            Greed compressor          ")
        print("                  by                  ")
        print("       Elias Bernardo - @ebmm01       ")
        print("       Erick Giffoni  - @ErickGiffoni ")
        print("                 2020                 ")
        print("======================================")
        self.get_menu_options();

    def get_menu_options(self) -> None:
        print("1 - Codificar arquivo")
        print("2 - Decodificar arquivo")
        print("0 - Sair/ Terminar execução")
    
    def get_option(self,valid_options: List[int]) -> int:
        option = int(input(f"\nEscolha uma opção dentre os valores válidos ({valid_options}): "))
        
        if option == 0:
            print("\n SSaindo... \n ")
            exit(0)
        elif not option in valid_options:
            print("\n Opção inválida. Tente novamente. \n")
            return self.get_option(valid_options)
        
        self.clear_terminal()
        return option

    class Encode:

        def get_encode_options(self):
            print("1 - Informar caminho manualmente")
            print("2 - Usar arquivo de exemplo")
            print("3 - Voltar para o menu principal")
        
        def get_decode_example_files(self):
            print("\n1 - Lorem Ipsum - 33.7 KiB (text.txt)")
            print("2 - Gutenberg's Frankenstein, by Mary Wollstonecraft - 440.2 KiB (text_2.txt)")
            print("3 - Operários, trabalho e política na indústria têxtil em Fernão Velho - Marcelo Góes Tavares (Tese) - 815.4 KiB (text_3.txt)")
            print("4 - Voltar para o menu principal\n")

        def encoding_text(self):
            print("\n Codificando arquivo...\n")

        def encode_text_success(self):
            print("\n Texto codificado com sucesso!!\n")

        def encode_text_fail(self, error):
            print("\nOcorreu um erro ao codificar o arquivo:\n", error)

    class Decode:
        
        def get_decode_options(self):
            print("\n1 - Informar caminho manualmente")
            print("2 - Usar arquivo de exemplo")
            print("3 - Voltar para o menu principal\n")
        

        def decoding_text(self):
            print("\n Decodificando arquivo...\n")
    
    
    