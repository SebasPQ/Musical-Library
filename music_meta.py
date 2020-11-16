import os
import music_tag

class musicMeta:
    def __init__(self,path):
        self.path=path
        self.asps = []
        self.titlePath = []
        self.artist = []
        self.genre = []

    def getMeta(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.aac') or file.endswith('.wav') or file.endswith('.ogg'):
                    self.asps.append(os.path.join(root, file))

    #se cambia por arboles cuando este implementado
    def actualizar(self): 
        self.getMeta() 
        for i in self.asps:
            f=music_tag.load_file(i)
            self.titlePath.append(i)
            self.artist.append(f['artist'])
            self.genre.append(f['genre'])

    def getTitlePath(self):
        self.actualizar()
        return self.titlePath

    def getArtist(self):
        self.actualizar()
        return self.artist

    def getGenre(self):
        self.actualizar()
        return self.genre
    
    def compare(self,array,element):
        playList=[]
        self.actualizar()
        contador=0
        if array == 'genre':
            for i in self.genre:
                if element == str(i):
                    playList.append(self.titlePath[contador])
                contador=contador+1
        if array == 'artist':
            for i in self.artist:
                if str(i) == element:
                    playList.append(self.titlePath[i])
        return playList