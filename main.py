from collections import Counter
from node import Node
from priority_queue import PriorityQueue
from bitstring import Bits, BitStream, BitArray
from encode import Encode
from decode import Decode

encode_util = Encode()
decode_util = Decode()

with open('text_3.txt', 'r', encoding='UTF-8') as file:
    file_content = ''.join(file.readlines())
    binary_file_content = BitStream(Bits(file))
    frequencies = encode_util.get_frequencies(file_content)

    #print(frequencies)
#print(priority_queue.lst)

parent = encode_util.get_node_tree(frequencies)

print("Sort finalizado")
print(parent)

hash_table = {}
parent.generate_hashT(hash_table, "")
x = binary_file_content.read(8)
print(hash_table)

encoded_text = encode_util.encode_text(file_content, hash_table)
inv_map = {v: k for k, v in hash_table.items()}
decoded_text = decode_util.decode_text(encoded_text, inv_map)

def get_largest_char_size(hash_table: dict) -> int:
    bigger_char_size = 0
    for char in list(hash_table.keys()):
        if  len(encode_char(char)) > bigger_char_size:
            bigger_char_size = len(encode_char(char))

    return bigger_char_size

def encode_char(symbol: str) -> str:
    return ''.join(format(ord(i), 'b') for i in symbol)

def encode_headers(node: 'Node', bitarray: 'BitArray', char_size: int):
    if node.isLeaf():
        bitarray.append('0b1')

        encoded_char = encode_char(node.symbol)
        encoded_char = "".join("0" for n in range(char_size - len(encoded_char))) + encoded_char
        bitarray.append(f"0b{encoded_char}")
    else:
        bitarray.append('0b0')
        encode_headers(node.left, bitarray, char_size)
        encode_headers(node.right, bitarray, char_size)

def decode_headers(bitStream: 'BitStream', char_size: int):
    if bitStream.read(1).bin == '1':
        encoded_char: str = bitStream.read(char_size).bin
        int_char: int = int(encoded_char,2)
        return Node(symbol=chr(int_char)[0], count=1)
    else:
        left = decode_headers(bitStream, char_size)
        right = decode_headers(bitStream, char_size)
        return Node(left=left, right=right, count=1)

def get_encoded_file_char_size(bitStream: 'BitStream') -> int:
    return int(bitStream.read(5).bin, 2)

def save_char_size_bits(bitStream: 'BitArray', char_size: int) -> 'BitArray':
    bitStream.append((char_size).to_bytes(2, byteorder='big'))
    return bitStream[-5:]

char_size = get_largest_char_size(hash_table)

encoded_header = BitArray()

encoded_header = save_char_size_bits(encoded_header, char_size)

encode_headers(parent, encoded_header, char_size)

decoded_header = decode_headers(BitStream(encoded_header), char_size)

print("")

import struct

bits = encoded_header.bin + encoded_text
fileEnc = BitArray('0b' + bits)

with open("test.eliaserick", "wb") as f:
    f.write(fileEnc.tobytes())


decCont = BitArray()
with open("test.eliaserick", "rb") as f2:
    content = f2.readlines()
    for line in content:
        decCont.append(line)


x = BitStream(decCont)
char_size = get_encoded_file_char_size(x)
decoded_header_2 = decode_headers(x, char_size)

hash_table = {}
decoded_header_2.generate_hashT(hash_table, "")
inv_map = {v: k for k, v in hash_table.items()}
decoded_text = decode_util.decode_text(decCont.bin[x.bitpos:x.len], inv_map)

print(decoded_text)

"""
TODO: 
ENCODE:

0 - Abrir o arquivo não codificado
1 - Gerar a contagem de frequências com base no arquivo
2 - Gerar a àrvore com base na frequência
3 - Gerar a hash de cada caractere
4 - Codificar o texto
5 - Gerar os headers de metadados 
6 - Salvar um novo arquivo com os headers + texto codificado

DECODE:

0 - Abrir o arquivo codificado
1 - Pegar o tamanho do array com base no valor descrito nos N primeiros bits.
2 - Pegar a àrvore codificada (??????)
3 - Pegar o texto codificado (restante dos bits)
4 - Gerar a tabela de decodificação
5 - Decodificar o texto com base na tabela de decodificação 
6 - Salvar um novo arquivo o conteúdo original
"""

