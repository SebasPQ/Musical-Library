from DLinkedLists import DoublyLinkedList


# Función ingresar canción
def new_song(songs_list, trees, song):
    songs_list.insert_at_start(song)
    for i in range(4):
        trees[i].insert(songs_list.start_node, i)


# Función remover canción
def remove_song(songs_list, trees, song_name):
    node = trees[0].search_tree(song_name)
    if node is not None:
        trees[0].delete_node(node.content.start_node.item.item[0])

        for i in range(1, 4):
            value = node.content.start_node.item.item[i]
            node_with_value = trees[i].search_tree(value)
            node_with_value.content.delete_element_by_value(node.content.start_node.item)
            if node_with_value.content.start_node is None:
                trees[i].delete_node(node_with_value.data)
        songs_list.delete_by_node(node.content.start_node.item)
    else:
        print("No se encontró la canción "+song_name)


# Función mostrar datos de la canción por nombre
def show_song(songs_list, song_name):
    node = songs_list.start_node
    while node is not None:
        if node.item[0].lower() == song_name:
            print(node.item)
            break
        node = node.nref
    if node is None:
        print("No se encontró la canción "+song_name)


# Función para identificar la frecuencia de un valor/atributo en la lista
def value_frecuency(songs_list, n):
    value_frec = []
    aux_node = songs_list.start_node

    while aux_node is not None:
        new_value = True
        for v in value_frec:
            if aux_node.item[n] == v[0]:
                v[1] = str(int(v[1])+1)
                new_value = False
        if new_value:
            value_frec.append([aux_node.item[n], '1'])
        aux_node = aux_node.nref
    return value_frec


# Función para identificar el genero más repetido
def favorite_genre(songs_list):
    genre_frec = value_frecuency(songs_list, 2)
    max_value = 0
    fav_genre = ''
    for e in genre_frec:
        if int(e[1]) > max_value:
            max_value = int(e[1])
            fav_genre = e[0]
    print(fav_genre)


# crear listas con artista y género más repetido junto con su respectiva frecuencia
def favorite_artist(songs_list):
    artist_frec = value_frecuency(songs_list, 1)
    max_value = 0
    fav_artist = ''
    for a in artist_frec:
        if int(a[1]) > max_value:
            max_value = int(a[1])
            fav_artist = a[0]
    print(fav_artist)
