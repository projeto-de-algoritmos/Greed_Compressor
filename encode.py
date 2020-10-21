from node import Node
from priority_queue import PriorityQueue
from collections import Counter
from typing import List, TextIO


class Encode:

    def get_node_tree(self, frequencies: List['Node']) -> 'Node':
        priority_queue = PriorityQueue(frequencies)

        while True:
            left_node = priority_queue.get_and_remove_first_element()
            right_node = priority_queue.get_and_remove_first_element()

            parent = Node(left=left_node, right=right_node)

            if (len(priority_queue) == 0):
                return parent
            
            priority_queue.add(parent)
    
    def get_frequencies(self, file_content: str) -> List['Nodes']:
        return [Node(count = count, symbol = elem) for elem, count in Counter(file_content).most_common()]

    def encode_text(self, text: str, encode_table: dict) -> str:
        encoded_text = ""
        for char in text:
            encoded_text += encode_table[char]
        
        return encoded_text