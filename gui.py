import PySimpleGUI as sg
from modules import functions

label = sg.Text('Type a To-Do')
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button('Add')


window = sg.Window("My-To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()