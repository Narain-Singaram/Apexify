import streamlit as st
import functions as f
import random as rand

def crt_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    f.write_todos(todos)
    print(todo)

def edit_todo(index):
    sel_edit_todo = st.session_state["edit_todo" + index]

def repeated_code():
    st.write("Created by: Narain Singaram")
    st.title("Apexify | To-Do List App")

todos = f.get_todos()

tab1, tab2 = st.tabs(["Main", "Edit"])

with tab1:
    repeated_code()
    st.text_input(label="Suggest a To-Do",
                  placeholder="What's on your mind?",
                  on_change=crt_todo,
                  key="new_todo")

    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            f.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
        else:
            pass
    if st.button('Shuffle Order'):
        rand.shuffle(todos)
    else:
        pass

with tab2:
    repeated_code()

    for index, todo in enumerate(todos):
        st.text_input(label="Edit " + todo + "in position" + " " + str(index + 1),
                      value=todo,
                      on_change=edit_todo(index),
                      key=f"edit_todo{index}")

