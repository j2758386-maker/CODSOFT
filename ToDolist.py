import streamlit as st
import os

FILE = "tasks.txt"

st.set_page_config(
    page_title="Smart To Do List",
    page_icon="📝",
    layout="centered"
)

# CSS Design
st.markdown("""
<style>

.block-container{
    max-width:700px;
    margin:auto;
}

h1{
    text-align:center;
}

.task-box{
    padding:10px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)


# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return f.read().splitlines()
    return []


# Save tasks
def save_tasks(tasks):
    with open(FILE,"w") as f:
        for t in tasks:
            f.write(t+"\n")


if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()


st.title("📝 Smart To Do List")
st.write("Manage your daily tasks easily 🚀")


new_task = st.text_input(
    "Enter your task"
)

col1,col2 = st.columns(2)

with col1:

    if st.button("➕ Add Task"):

        if new_task:

            st.session_state.tasks.append(new_task)

            save_tasks(
                st.session_state.tasks
            )

            st.success("Task Added")


with col2:

    if st.button("🗑 Clear All"):

        st.session_state.tasks=[]

        save_tasks([])

        st.warning("All Tasks Cleared")


st.subheader("Your Tasks")

for i,task in enumerate(
    st.session_state.tasks
):

    col1,col2 = st.columns([5,1])


    with col1:
        st.info(f"✅ {task}")


    with col2:

        if st.button(
            "❌",
            key=i
        ):

            st.session_state.tasks.pop(i)

            save_tasks(
                st.session_state.tasks
            )

            st.rerun()