import time
import random

from Avl_tree import AVLTree
from DLinkedLists import DoublyLinkedList
from Songs_functions import *


# Lista total de canciones:
songs = DoublyLinkedList()
# Lista de canciones favoritas:
my_songs = DoublyLinkedList()
# Árboles de atributos
songs_names_tree = AVLTree()
#artists_tree = AVLTree()
#genres_tree = AVLTree()
#years_tree = AVLTree()
#trees = [songs_names_tree, artists_tree, genres_tree, years_tree]

trees = [songs_names_tree]
genres=['pop', 'rock', 'regaeton', 'jazz', 'salsa', 'cumbia', 'soul', 'metal', 'rap', 'vallenato']
n=100000
start1 = time.time()
for i in range(n):
    random1 = random.randint(0, 9)
    random2 = random.randint(0, 20)
    random3 = random.randint(1900, 2020)
    new_song(songs, trees, [str(i), str(random2), genres[random1], str(random3)])
end1 = time.time()

# songs.traverse_list()
# songs_names_tree.print_tree()


print("listo"+'\n')
start = time.time()
for i in range(n):
    show_song(trees,str(i))
end = time.time()
print(str(end - start)+' para mostrar '+str(n)+' canciones')

start = time.time()
print('tu genero favorito es ')
favorite_genre(songs)
end = time.time()
print(str(end - start)+' para mostrar genero favorito con '+str(n)+' canciones')

start = time.time()
print('tu artista favorito es ')
favorite_artist(songs)
end = time.time()
print(str(end - start)+' para mostrar artista favorito con '+str(n)+' canciones')

start2 = time.time()
for i in range(n):
    remove_song(songs, trees, str(i))
end2 = time.time()

print(str(end1 - start1)+' para insertar '+str(n)+' canciones')
print(str(end2 - start2)+' para borrar '+str(n)+' canciones')












'''
new_song(songs, trees, ['Is it true', 'Tame impala', 'Pop', '2020'])
new_song(songs, trees, ['Blinding Lights', 'The Weeknd', 'Pop', '2019'])
new_song(songs, trees, ['Do I wanna know', 'Artic Monkeys', 'Rock', '2013'])
new_song(songs, trees, ['The less I know the better', 'Tame impala', 'Pop', '2015'])
new_song(songs, trees, ['Holiday', 'Green day', 'rock', '2010'])
'''
'''
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
'''
