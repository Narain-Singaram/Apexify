import streamlit as st
import functions as f
import random

st.set_page_config(page_title="Apexify", layout="centered", initial_sidebar_state = "auto")
def opn_scss_file(css_file):
    with open(css_file) as css_f:
        st.markdown(f'<style>{css_f.read()}</style>', unsafe_allow_html=True)

opn_scss_file("style.scss")
def crt_todo():
    todo = st.session_state["new_todo"].title()
    todos.append(todo + "\n")
    st.info(f'{todo} successfully created as a todo.', icon="ℹ️")
    f.write_todos(todos, "todo_list.rtf")
def edit_todo(index):
    # sel_edit_todo = st.session_state["edit_todo" + str(index)]
    # todos[str(index - 1)] = sel_edit_todo
    pass

title = "Apexify | To-Do List App"
def repeated_code():
    st.write("Created by: Narain Singaram")
    st.title(title)

todos = f.read_todos("todo_list.rtf")
dl_todos = f.read_todos("download_todo_list.txt")
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
            f.write_todos(todos, "todo_list.rtf")
            del st.session_state[todo]
            st.experimental_rerun()
        else:
            pass
    if st.button('Shuffle Order'):
        try:
            todo.capitalize()
        except NameError:
            st.error('There are no todos to shuffle in the todo list', icon="🚨")
        else:
            st.info('The To-Do List has been shuffled.', icon="ℹ️")
            random.shuffle(todos)
            f.write_todos(todos, "todo_list.rtf")

    with open('todo_list.rtf','r') as t_lst, open('download_todo_list.txt','a') as dl_file:
        dl_file.writelines("\n" + title + " --- Created By: Narain Singaram")
        for l in t_lst:
            dl_file.writelines(l)

    with open("download_todo_list.txt", "rb") as dl_file:
        st.download_button(
            label="Download To-Do List",
            data=dl_file,
            file_name="download_todo_list.txt",
        )

with tab2:
    repeated_code()
    st.subheader ("Edit Feature in progress. Currently under maintenance")
    for index, todo in enumerate(todos):
        st.text_input(label="Edit " + todo + "in position" + " " + str(index + 1),
                      value=todo,
                      on_change=edit_todo(index),
                      key="edit_todo" + str(index))
    pass
