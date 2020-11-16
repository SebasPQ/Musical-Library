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
trees = [songs_names_tree, artists_tree, genres_tree, years_tree]

new_song(songs, trees, ['Is it true', 'Tame impala', 'Pop', '2020'])
new_song(songs, trees, ['Blinding Lights', 'The Weeknd', 'Pop', '2019'])
new_song(songs, trees, ['Do I wanna know', 'Artic Monkeys', 'Rock', '2013'])
new_song(songs, trees, ['The less I know the better', 'Tame impala', 'Pop', '2015'])
new_song(songs, trees, ['Holiday', 'Green day', 'rock', '2010'])
new_song(songs, trees, ['a', 'x', 'w', '2000'])
new_song(songs, trees, ['b', 'x', 'v', '2001'])
new_song(songs, trees, ['c', 'y', 'w', '2002'])
new_song(songs, trees, ['d', 'y', 'v', '2003'])

print('\n' + 'arbol de canciones --------------------------------------------------------' + '\n')
songs_names_tree.print_tree()
print('\n'+'arbol de artistas --------------------------------------------------------'+'\n')
artists_tree.print_tree()
print('\n'+'arbol de generos --------------------------------------------------------'+'\n')
genres_tree.print_tree()
print('\n'+'arbol de años --------------------------------------------------------'+'\n')
years_tree.print_tree()
print('\n' + "canciones")
songs.traverse_list()

print()
# show_song(trees, 'The less i know the better')
# favorite_genre(songs)
# favorite_artist(songs)

remove_song(songs, trees, 'is it true')

print()
print('\n'+'arbol de canciones --------------------------------------------------------'+'\n')
songs_names_tree.print_tree()
print('\n'+'arbol de artistas --------------------------------------------------------'+'\n')
artists_tree.print_tree()
print('\n'+'arbol de generos --------------------------------------------------------'+'\n')
genres_tree.print_tree()
print('\n'+'arbol de años --------------------------------------------------------'+'\n')
years_tree.print_tree()

print('\n' + "canciones")
songs.traverse_list()

print()
show_song(trees, 'Holiday')