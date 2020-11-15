# AVL Binary search tree implementation in Python
# Author: AlgorithmTutor

# data structure that represents a node in the tree
from Avl_tree import AVLTree

if __name__ == '__main__':
    bst = AVLTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    bst.prettyPrint()
    bst.deleteNode(4)
    bst.prettyPrint()
