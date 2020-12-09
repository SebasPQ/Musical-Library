import subprocess
import sys

#por el omento uno tiene que agregar la ubicacion de su reproductor
def play(array,path):
    a=array
    a.insert(0,path)
    subprocess.run(a) 