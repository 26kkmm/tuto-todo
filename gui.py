import PySimpleGUI as sg
from modules import functions

label = sg.Text('Type a To-Do')
input_box = sg.InputText(tooltip="Enter ToDo", key='todo')
add_button = sg.Button('Add')

window = sg.Window("My-To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()