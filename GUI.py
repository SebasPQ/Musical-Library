import PySimpleGUI as sg
from music_meta import musicMeta
from pathlib import PureWindowsPath, Path
import play
from json import (load as jsonload, dump as jsondump)
from os import path

sg.theme('BluePurple')
SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'path': None, 'reproductor': None}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'path': '-PATH-', 'reproductor': '-REPRODUCTOR-'}

#cargar las configuraciones
def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')


#funcion para crear las ventanas
def createConfigWindow(settings):
    folder=settings['path']
    reproductor=settings['reproductor']
    layout = [[sg.Text('Folder to open')],
            [sg.In(folder,key='-PATH-'), sg.FolderBrowse()],
            [sg.Text('Defult reproductor')],
            [sg.In(reproductor,key='-REPRODUCTOR-'),sg.FileBrowse()],
            [sg.Button('Ok')]] 

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # update window with the values read from settings file
        try:
            if SETTINGS_KEYS_TO_ELEMENT_KEYS[key] == '-PATH-':
                folder=settings[key]
            elif SETTINGS_KEYS_TO_ELEMENT_KEYS[key] == '-REPRODUCTOR-':
                reproductor=settings[key]
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return sg.Window('MusicLib', layout)

def createChoicerWindow(category,subCategory):
    layout = [[sg.Listbox(values=(category), size=(20,3),key='-TREE-',enable_events=True), sg.Listbox(values=(subCategory),size=(20,3),key='-LEAF-')],      
                [sg.OK()]]
    return sg.Window('MusicLib', layout)         

def createViewerWindow(playList,sobra):
    layout = [[sg.Listbox(values=(playList), size=(20,3),key='-PLAYLIST-',enable_events=True), sg.Listbox(values=(sobra),size=(20,3),key='-NOTPLAY-')],      
                [sg.Button('Like'),sg.T('                           '),sg.Button('Add')],
                [sg.Button('Play')]]
    return sg.Window('MusicLib', layout) 

#otras funciones
def getSub(music,category):
    return music.showTree(category)

def getViewList(music,category,subCategory):
    return music.getItems(category,subCategory)

def getPlayList(music,items):
    return music.getPlayList(items)

#main
def GUI():
    procede=True
    category=['genre','artist','year']
    subCategory=[]
    playList=[]
    sobra=[]
    config = load_settings(SETTINGS_FILE,DEFAULT_SETTINGS)
    
    window = createConfigWindow(config)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            procede=False
            break
        if event == 'Ok':
            c= Path(values['-PATH-'])
            d=Path(values['-REPRODUCTOR-'])
            reproductor=PureWindowsPath(d)
            b= PureWindowsPath(c)
            music= musicMeta(b)
            music.actualizar()
            # agregar metodo que crea los arboles
            save_settings(SETTINGS_FILE, config, values)
            break
    window.close()

    window = createChoicerWindow(category,subCategory)
    playList=[]
    while procede:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            procede=False
            break
        if values['-TREE-']:
            leaf=getSub(music,values['-TREE-'][0])
            window['-LEAF-'].update(leaf)
        if event == 'OK' and values['-LEAF-']:
            #agregar el metodo que crea la playlist y la devuelve como un array
            playList=getViewList(music,values['-TREE-'][0],values['-LEAF-'][0])
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
            print('aun no implementado')
        if event == 'Add':
            #lo mismo que el anterior solo que con agregar
            print('aun no implementado')
        if event == 'Play':
            #transformar la DList en un array
            items=getPlayList(music,playList)
            play.play(items,reproductor)
    window.close()

GUI()