import streamlit as st

# Set up page
st.set_page_config(
    page_title="Interactive Reading App",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed")

############# Intro Page ############################
########## Title ###################
st.markdown(
    """
    <h1 style='text-align: center;'>Interactive Reading App 📖</h1>
    """,
    unsafe_allow_html=True
)

## Create space
st.write('')
st.write('')

### Page Image #####
_, newcol, _ = st.columns([1, 3, 1])
with newcol:
    st.image('imag/pic1.jpg')
    st.write('')
    st.markdown('###### **Take your reading skills to the next level with our Interactive Reading App.** ')
    

### START #####    
_, col1, _ = st.columns(3, gap='large')
with col1:
    if st.button('Start', use_container_width=True):
        st.switch_page('pages/1_TakePhoto_btn.py')
