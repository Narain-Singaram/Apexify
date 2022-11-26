import streamlit as st
import functions as f

def crt_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    f.write_todos(todos)
    print(todo)


todos = f.get_todos()

st.write("Created by: Narain Singaram")
st.title("Apexify | To-Do List App")

st.text_input(label="Suggest a To-Do",
              placeholder="What's on your mind?",
              on_change=crt_todo,
              key="new_todo")


for todo in todos:
    st.checkbox(todo)