import PySimpleGUI as sg
from modules import functions

label = sg.Text("Type a To-Do")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("add")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10)
)
button_edit = sg.Button("edit")
button_done = sg.Button("done")
button_exit = sg.Button("exit")

window = sg.Window(
    "My-To-Do App",
    layout=[[label], [input_box, add_button], [list_box, button_edit, button_done]],
    font=("Helvetica", 20),
)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case 'edit':
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

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
