import subprocess
import sys

#por el omento uno tiene que agregar la ubicacion de su reproductor
def play(array):
    a=array
    a.insert(0,r'C:\Program Files\VideoLAN\VLC\vlc.exe')
    subprocess.run(a)