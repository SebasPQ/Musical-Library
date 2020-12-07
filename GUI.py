import PySimpleGUI as sg
from music_meta import musicMeta
from pathlib import PureWindowsPath, Path
import play

sg.theme('BluePurple')

choices=('genre','artist','year')
#por el momento van a ser 3 

def createConfigWindow():
    layout = [[sg.Text('Folder to open')],
            [sg.In(), sg.FolderBrowse(key='-PATH-')],
            [sg.Text('Defult reproductor')],
            [sg.In(),sg.FolderBrowse(key='-REPRODUCTOR-')],
            [sg.Button('Ok')]]
    return sg.Window('MusicLib', layout)

def createChoicerWindow(category,subCategory):
    layout = [[sg.Listbox(values=(category), size=(20,3),key='-TREE-',enable_events=True), sg.Listbox(values=(subCategory),size=(20,3),key='-LEAF-')],      
                [sg.OK()]]
    return sg.Window('MusicLib', layout)         

def createViewerWindow(playList,sobra):
    layout = [[sg.Listbox(values=(playList), size=(20,3),key='-PLAYLIST-',enable_events=True), sg.Listbox(values=(sobra),size=(20,3),key='-NOTPLAY-')],      
                [sg.Button('Delete'),sg.T('                         '),sg.Button('Add')],
                [sg.Button('Play')]]
    return sg.Window('MusicLib', layout) 


def getSub(category):
    #agregar metodo que llame a un array que contenga los elementos de cada categoria
    return 

def main():
    procede=True
    category=['genre','artist','year']
    subCategory=[]
    playList=[]
    sobra=[]
    window = createConfigWindow()
    event, values = window.read()
    if event == 'OK':
        c= Path(values['-PATH-'])
        d=Path(values['-REPRODUCTOR-'])
        reproductor=PureWindowsPath(d)
        b= PureWindowsPath(c)
        a= musicMeta(b)
        a.actualizar()
        # agregar metodo que crea los arboles
    elif event == sg.WIN_CLOSED:
        procede=False
    window.close()

    window = createChoicerWindow(category,subCategory)
    while procede:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            procede=False
            break
        if values['-TREE-']:
            getSub(values['-TREE-'])
        if event == 'OK' and values['-LEAF-']:
            #agregar el metodo que crea la playlist y la devuelve como un array
            break
    window.close()

    window = createViewerWindow(playList,sobra)
    while procede:  
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Delete':
            #agregar metodo que elimina la cancion de la playlist y crea un nuevo arry
            #o uno que lo elimine dirrectamente del array
            break
        if event == 'Add':
            #lo mismo que el anterior solo que con agregar
            break
        if event == 'Play':
            #transformar la DList en un array
            playList= []
            play.play(playList,reproductor)
    window.close()

main()