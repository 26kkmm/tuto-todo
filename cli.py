from modules import functions
import time

now = time.strftime("%b-%d-%Y %H:%M:%S")
print("It is",now)

while True:
    user_action = input("Add | Show | Edit | Complete | Exit: ").strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        if len(todos) == 0:
            print("No todos")
        for index, todo in enumerate(todos):
            todo = todo.strip("\n").title()
            row = f"{index + 1} - {todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("New todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip("\n").title()
            todos.pop(number)

            functions.write_todos(todos)

            message = f' "{todo_to_remove}" is removed from the list.'
            print(message)
        except Exception:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")
