from Avl_tree import AVLTree
from DLinkedLists import DoublyLinkedList

# Lista total de canciones:
songs = DoublyLinkedList()
# Lista de canciones favoritas:
my_songs = DoublyLinkedList()


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
    bst.print_tree()
    bst.delete_node(4)
    bst.print_tree()

my_list = DoublyLinkedList()
my_list.insert_at_start(1)
my_list.insert_at_start(0)
my_list.insert_at_end(4)
my_list.insert_at_end(3)
my_list.insert_before_item(4,5)
my_list.traverse_list()