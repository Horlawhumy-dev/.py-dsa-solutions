""" Binray Search Tree Implementation"""
from .node import Node

class BT:
    def __init__(self, root, name):
        self.tree = []
        self.root = root
        self._name = name
    
    def is_empty(self):
        return not self.tree

    def __str__(self):
        return str(self.tree)


if __name__ == '__main__':
    root = Node(5)
    bt = BT(root, 'MINIMUM BINARY TREE')
    print(bt)
    print(bt.is_empty())