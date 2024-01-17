import streamlit as st
from modules import functions

st.title("My ToDo App")
st.subheader("This is my app")
st.write("Write your ToDo, Aha!")

todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder='Add ToDo...')