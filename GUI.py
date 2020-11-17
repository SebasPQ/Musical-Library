import PySimpleGUI as sg
from music_meta import musicMeta
from pathlib import PureWindowsPath, Path
import play

sg.theme('BluePurple')

procede=False
choices=('genre','artist')

layout = [[sg.Text('Document to open')],
          [sg.In(), sg.FolderBrowse(key='-PATH-')],
          [sg.Open(button_text='Actualizar')],
          [sg.Text('organizacion a escoger')],
          [sg.Listbox(choices, size=(15, len(choices)), key='-CHOICES-')],
          [sg.Button('Ok')]]

window = sg.Window('MusicLib', layout)

#por el momento no se actualiza con los generos que se encuentren en la lista
#y solo funciona la reproduccionpor genero por la razon anterior
while True:  
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Actualizar':
        c= Path(values['-PATH-'])
        b= PureWindowsPath(c)
        a= musicMeta(b)
    if event == 'Ok':
        if values['-CHOICES-'][0]=='genre':
            choices= ('Vocal','pizza','sountrack>')
            layout=[[sg.Text('organizacion a escoger')],
                    [sg.Listbox(choices, size=(15, len(choices)), key='-CHOICES-')],
                    [sg.Button('Play')]]
            procede=True
            break
        if values['-CHOICES-'][0]=='artist':
            break
window.close()
if procede:
    window=sg.Window('MusicLib', layout)
    event, values = window.read()
    if event == 'Play':
        playList= a.compare('genre',values['-CHOICES-'][0])
        play.play(playList)
    window.close()