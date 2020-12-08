import os
import music_tag
from Avl_tree import AVLTree
from DLinkedLists import DoublyLinkedList

class musicMeta:
    def __init__(self,path):
        self.path=path
        self.asps = []
        self.songs_names_tree = AVLTree()
        self.artist = AVLTree()
        self.genre = AVLTree()
        self.year = AVLTree()
        self.songs= DoublyLinkedList()
        self.trees = [self.songs_names_tree, self.artist, self.genre, self.year]

    def getMeta(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.aac') or file.endswith('.wav') or file.endswith('.ogg') or file.endswith('mp4'):
                    self.asps.append(os.path.join(root, file))

    def actualizar(self): 
        self.getMeta() 
        for i in self.asps:
            f=music_tag.load_file(i)
            self.songs.insert_at_start([f['title'],f['artist'],f['genre'],f['year'],i])
            for x in range(len(self.trees)):
                self.trees[x].insert(self.songs.start_node,x)
        self.asps.clear()
    
    def delete(self,song_name):
        node = self.trees[0].search_tree(song_name.lower())
        if node is not None:
            self.trees[0].delete_node(song_name.lower())
            for i in range(1, 4):
                value = node.content.start_node.item.item[i]
                node_with_value = self.trees[i].search_tree(value.lower())
                node_with_value.content.delete_by_node(node.content.start_node)
                if node_with_value.content.start_node is None:
                    self.trees[i].delete_node(node_with_value.data.lower())
            self.songs.delete_by_node(node.content.start_node.item)
        else:
            print("No se encontró la canción "+song_name)

    def show_song(self, song_name):
        node = self.trees[0].search_tree(str(song_name).lower())
        if node is not None:
            print(node.content.start_node.item.item)
        else:
            print("No se encontró la canción "+song_name)

    def showTree(self,category):
        node=None
        if category=='artist':
            node=self.trees[1].root.content
            tree=1
        elif category=='genre':
            node=self.trees[2].root.content
            tree=2
        elif category=='year':
            node=self.trees[3].root.content
            tree=3
        array=node.dListToArray(tree)
        return array

 '''
    def getItems(self,category,subCategory):
        node=None
        if category=='artist':
            node=self.trees[1].root.content
            tree=1
        elif category=='genre':
            node=self.trees[2].root.content
            tree=2
        elif category=='year':
            node=self.trees[3].root.content
            tree=3
        
#pruebas
z= musicMeta(r'C:\Users\guion\Music')
z.actualizar()
print(z.showTree('year'))