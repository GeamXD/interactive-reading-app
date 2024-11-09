import streamlit as st
import os
# import logic as lg

st.set_page_config(
    page_title="Overview",
    page_icon="📸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except:
        pass


st.title('Uploaded Pages')
try:
    st.image('image_1.jpg', use_container_width=True)
except Exception as e:
    st.error('Page not uploaded')


bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Photos', use_container_width=True):
        delete_file('image_1.jpg')
        st.switch_page('pages/2_TakePhoto.py')
with bt_3:
    if st.button('Start Reading', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')