import streamlit as st

st.set_page_config(
    page_title="Take Photo",
    page_icon=":material/camera:",
    layout="centered",
    initial_sidebar_state="collapsed")

_, col1, _ = st.columns([1, 3, 1])
with col1:
    if st.button('Take a Picture', use_container_width=True):
        st.switch_page('pages/2_TakePhoto.py')