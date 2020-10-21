from collections import Counter
from node import Node
from priority_queue import PriorityQueue
from bitstring import Bits, BitStream, BitArray
from encode import Encode
from decode import Decode

encode_util = Encode()
decode_util = Decode()

with open('text.txt', 'r', encoding='UTF-8') as file:
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

"""
void EncodeNode(Node node, BitWriter writer)
{
    if (node.IsLeafNode)
    {
        writer.WriteBit(1);
        writer.WriteByte(node.Value);
    }
    else
    {
        writer.WriteBit(0);
        EncodeNode(node.LeftChild, writer);
        EncodeNode(node.Right, writer);
    }
}
"""


def encode_headers(node: 'Node', bitarray: 'BitArray'):
    if node.isLeaf():
        bitarray.append('0b1')

        encoded_char = ''.join(format(ord(i), 'b') for i in node.symbol)
        encoded_char = "".join("0" for n in range(7 - len(encoded_char))) + encoded_char
        bitarray.append(f"0b{encoded_char}")
    else:
        bitarray.append('0b0')
        encode_headers(node.left, bitarray)
        encode_headers(node.right, bitarray)


"""
Node ReadNode(BitReader reader)
{
    if (reader.ReadBit() == 1)
    {
        return new Node(reader.ReadByte(), null, null);
    }
    else
    {
        Node leftChild = ReadNode(reader);
        Node rightChild = ReadNode(reader);
        return new Node(0, leftChild, rightChild);
    }
}
"""
def decode_headers(bitStream: 'BitStream'):
    if bitStream.read(1).bin == '1':
        encoded_char = bitStream.read(7).bin
        int_char = int(encoded_char,2)
        return Node(symbol=chr(int_char)[0], count=1)
    else:
        left = decode_headers(bitStream)
        right = decode_headers(bitStream)
        return Node(left=left, right=right, count=1)

encoded_header = BitArray()

encode_headers(parent, encoded_header)

decoded_header = decode_headers(BitStream(encoded_header))

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
decoded_header_2 = decode_headers(x)

hash_table = {}
decoded_header_2.generate_hashT(hash_table, "")
inv_map = {v: k for k, v in hash_table.items()}
decoded_text = decode_util.decode_text(decCont.bin[x.bitpos:x.len], inv_map)

print(decoded_text)
print(content)
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

