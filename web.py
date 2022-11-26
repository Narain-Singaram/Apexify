import streamlit as st
import functions as f

todos = f.get_todos()

st.write("Created by: Narain Singaram")
st.title("Apexify | To-Do List App")

st.text_input(label="Suggest a To-Do", placeholder="What's on your mind?")

for todo in todos:
    st.checkbox(todo)