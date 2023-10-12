import streamlit as sl
import functions

todos = functions.opens_file()

def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.closes_file(todos)


sl.title("My Todo app")
sl.subheader("This is my todo app!")
sl.write("To delete an item check the box")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.closes_file(todos)
        del sl.session_state[todo]
        sl.rerun()

sl.text_input(label="Add", placeholder="Add a new todo here!",
              on_change=add_todo, key="new_todo")
