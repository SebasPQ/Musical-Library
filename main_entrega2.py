import time
import random

from Avl_tree import AVLTree
from DLinkedLists import DoublyLinkedList
from Songs_functions import *


# Lista total de canciones:
songs = DoublyLinkedList()

# Árboles de atributos
songs_names_tree = AVLTree()

#artists_tree = AVLTree()
#genres_tree = AVLTree()
#years_tree = AVLTree()
#trees = [songs_names_tree, artists_tree, genres_tree, years_tree]

trees = [songs_names_tree]
genres = ['pop', 'rock', 'regaeton', 'jazz', 'salsa', 'cumbia', 'soul', 'metal', 'rap', 'vallenato']
n = 10000

start1 = time.time()
# crear n canciones con datos "aleatorios"
for i in range(n):
    random1 = random.randint(0, 9)
    random2 = random.randint(0, 20)
    random3 = random.randint(1900, 2020)
    new_song(songs, trees, [str(i), str(random2), genres[random1], str(random3)])
end1 = time.time()


'''
print("listo"+'\n')
start = time.time()
for i in range(n):
    show_song(trees,str(i))
end = time.time()
print(str(end - start)+' para mostrar '+str(n)+' canciones')
'''

start = time.time()
print('tu genero favorito es ')
favorite_genre(songs)
end = time.time()
print('tiempo: '+str(end - start)+' para mostrar genero favorito con '+str(n)+' canciones')

start = time.time()
print('tu artista favorito es ')
favorite_artist(songs)
end = time.time()
print('tiempo: '+str(end - start)+' para mostrar artista favorito con '+str(n)+' canciones')

print()
print('Datos de la canción:')
show_song(trees, '2500')


start2 = time.time()
for i in range(n):
    remove_song(songs, trees, str(i))
end2 = time.time()

print('tiempo: '+str(end1 - start1)+' para insertar '+str(n)+' canciones')
print('tiempo: '+str(end2 - start2)+' para borrar '+str(n)+' canciones')

print()
