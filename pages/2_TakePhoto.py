import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Take Photos",
    page_icon=":material/photo_camera:",
    layout="centered",
    initial_sidebar_state="collapsed")

st.markdown('##### Take a Picture')
picture = st.camera_input("Image Captured", label_visibility='collapsed')


# Create a file uploader for images
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

# Saves captured image
if picture:
    with open('image_1.jpg', 'wb') as f:
        pic = picture.read()
        f.write(pic)

if uploaded_file:
    image = Image.open(uploaded_file)
    image.save('image_1.jpg', format='JPEG')

bt_1, bt_2 = st.columns(2)
with bt_1:
    if st.button('Start Exercise', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')
with bt_2:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')