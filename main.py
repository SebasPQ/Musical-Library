from Avl_tree import AVLTree
from DLinkedLists import DoublyLinkedList
from Songs_functions import *


# Lista total de canciones:
songs = DoublyLinkedList()
# Lista de canciones favoritas:
my_songs = DoublyLinkedList()
# Árboles de atributos
songs_names_tree = AVLTree()
artists_tree = AVLTree()
genres_tree = AVLTree()
years_tree = AVLTree()
trees=[songs_names_tree, artists_tree, genres_tree, years_tree]

new_song(songs, trees, ['Is it true', 'Tame impala', 'Pop', '2020'])
new_song(songs, trees, ['Blinding Lights', 'The Weeknd', 'Pop', '2019'])
new_song(songs, trees, ['Do I wanna know', 'Artic Monkeys', 'Rock', '2013'])
new_song(songs, trees, ['The less I know the better', 'Tame impala', 'Pop', '2015'])

print('arbol de canciones')
songs_names_tree.print_tree()
print('arbol de artistas')
artists_tree.print_tree()
print('arbol de generos')
genres_tree.print_tree()
print('arbol de años')
years_tree.print_tree()
songs.traverse_list()

remove_song(songs, trees, 'Is it true')

print('arbol de canciones')
songs_names_tree.print_tree()
print('arbol de artistas')
artists_tree.print_tree()
print('arbol de generos')
genres_tree.print_tree()
print('arbol de años')
years_tree.print_tree()

songs.traverse_list()

"""""
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
my_list.insert_before_item(4, 5)
my_list.traverse_list()
"""

