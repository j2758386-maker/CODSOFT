import streamlit as st

st.set_page_config(
    page_title="CALCULATOR",
    page_icon="🔢",
    layout="centered"
)

st.title("CALCULATOR")

st.markdown("""
<style>
.block-container {
    max-width: 600px;
    margin: auto;
    padding: 25px;
    border: 3px solid black;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

if "expression" not in st.session_state:
    st.session_state.expression=""
st.markdown(
    f"""
    <div style="
        font-size:35px;
        text-align:right;
        padding:15px;
        border:2px solid #ccc;
        border-radius:10px;
        margin-bottom:20px;">
        {st.session_state.expression}
    </div>
    """,
    unsafe_allow_html=True
)

def press(value):
    st.session_state.expression+=str(value)
    st.rerun()

col1, col2, col3, col4= st.columns(4)

with col1:
    if st.button("7",use_container_width=True):
        press("7")
with col2:
    if st.button("8",use_container_width=True):
        press("8")
with col3:
    if st.button("9",use_container_width=True):
        press("9")
with col4:
    if st.button("➗",use_container_width=True):
        press("/")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4",use_container_width=True):
        press("4")
with col2:
    if st.button("5",use_container_width=True):
        press("5")
with col3:
    if st.button("6",use_container_width=True):
        press("6")
with col4:
    if st.button("✖️",use_container_width=True):
        press("*")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1",use_container_width=True):
        press("1")
with col2:
    if st.button("2",use_container_width=True):
        press("2")
with col3:
    if st.button("3",use_container_width=True):
        press("3")
with col4:
    if st.button("➖",use_container_width=True):
        press("-")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("C",use_container_width=True):
        st.session_state.expression = ""
        st.rerun()
with col2:
    if st.button("0",use_container_width=True):
        press("0")
with col3:
    if st.button("🟰",use_container_width=True):
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
        st.rerun()
with col4:
    if st.button("➕",use_container_width=True):
        press("+")
