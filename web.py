import streamlit as st
from modules import functions

todos = functions.get_todos()
def add_todo():
    todo =st.session_state['new-todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



st.title("My ToDo App")
st.subheader("This is my app")
st.write("Write your ToDo, Aha!")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder='Add ToDo...', key='new-todo', on_change=add_todo)