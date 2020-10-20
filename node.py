from typing import Tuple

class Node:

    def __init__(self, left: 'Node' = None, right: 'Node' = None, symbol: str = None, count: int = 0):
        self.symbol = symbol or "+"
        self.left = left
        self.right = right
        self.count = count

    def isLeaf(self) -> bool:
        return self.left == None and self.right == None

    def getCount(self) -> int:
        if (self.isLeaf()):
            return self.count
        return self.left.getCount() + self.right.getCount()

    def __generateHashT__(self, table: dict, key: str):
        if(self.isLeaf()):
            table.update({key: self.symbol})
            return

        self.left.__generateHashT__(table, key + "0")
        self.right.__generateHashT__(table, key + "1")
    
