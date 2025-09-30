import streamlit as st
import functions


todos=functions.get_todos()
def add_todo():
     todo=st.session_state["new_todo"] + "\n"
     todos.append(todo)
     functions.write_todos(todos)
     st.session_state.new_todo = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase productivity.")

todos_to_keep = []

for index, todo in enumerate(todos):
    checked = st.checkbox(todo.strip(), key=f"todo_{index}")
    if not checked:  # keep unchecked todos
        todos_to_keep.append(todo)

# Update todos if any were removed
if len(todos_to_keep) != len(todos):
    todos = todos_to_keep
    functions.write_todos(todos)



st.text_input(label=" ", placeholder="Add new todo",
              key="new_todo",
              on_change=add_todo)

