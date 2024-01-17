import PySimpleGUI as sg
from modules import functions
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('black')
clock = sg.Text('', key='clock')
label = sg.Text("Type a ToDo")
input_add = sg.InputText(tooltip="Enter ToDo", key="todo")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=(40, 10)
)

button_add = sg.Button(image_source='add.png', tooltip='Add ToDo', size=10, key='add')
button_edit = sg.Button("edit")
button_done = sg.Button('done', tooltip='Done', size=8)
button_exit = sg.Button("exit")

window = sg.Window(
    "My ToDo App",
    layout=[[clock], [label], [input_add, button_add],
            [list_box, button_edit, button_done],
            [button_exit]],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read()
    print(event)
    print(values)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'edit':
            try:
                window['todo'].update(value='')
                todos = functions.get_todos()
                todo_to_edit = values["todos"][0]

                new_todo = sg.popup_get_text('Edit todo:', 'Edit',
                                             default_text=todo_to_edit)

                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select a ToDo")

        case 'done':
            todos = functions.get_todos()
            done = values['todo']
            todos.remove(done)
            functions.write_todos(todos)

            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'exit':
            break

        case sg.WIN_CLOSED:
            break
window.close()
