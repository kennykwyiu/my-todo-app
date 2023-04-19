import streamlit as st
import functions

to_do_list = functions.get_to_do_list("to_do_list.txt")
def add_todo():
    to_do = st.session_state["new_todo"]
    to_do_list.append(to_do + '\n')
    functions.write_to_do_list(to_do_list)
    return to_do_list
st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, to_do in enumerate(to_do_list):
    checkbox = st.checkbox(to_do, key=to_do)
    if checkbox:
        to_do_list.pop(index)
        functions.write_to_do_list(to_do_list)
        del st.session_state[to_do]
        st.experimental_rerun()


st.text_input(label="Enter a todo:", placeholder="add new todo...",
              on_change=add_todo, key='new_todo')

# # add button "Completed"
# st.button("**Del Completed**", key="completed_todo")
