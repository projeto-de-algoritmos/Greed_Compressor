from collections import Counter
from node import Node
from priority_queue import PriorityQueue

with open('text.txt', 'r', encoding='UTF-8') as file:
    file_content = ''.join(file.readlines())
    frequencies = [Node(count = count, symbol = elem) for elem, count in Counter(file_content).most_common()]

    print(frequencies)

priority_queue = PriorityQueue(frequencies)
print(priority_queue.lst)

while True:
    # TODO
    left_node = priority_queue.get_and_remove_first_element()
    right_node = priority_queue.get_and_remove_first_element()

    parent = Node(left=left_node, right=right_node)

    if (len(priority_queue) == 0):
        # TODO return parent
        break
    
    priority_queue.add(parent)

print("Sort finalizado")
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

