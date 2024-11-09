import streamlit as st
import logic as lg
from msc import remove_markdown_formatting
import os

st.set_page_config(
    page_title="FeedBack",
    page_icon=":material/comment:",
    layout="centered",
    initial_sidebar_state="collapsed")

st.title('Feedback')
st.caption('Provide feedback on the accuracy of the spoken text.')

# Initialize a state variable for tracking which report to display
if 'active_report' not in st.session_state:
    st.session_state['active_report'] = 'reading'  # Default to reading report

# Report display container
with st.container(border=True):
    try:
        if st.session_state['active_report'] == 'reading' and st.session_state.get('reading_report'):
            st.markdown(st.session_state['reading_report'])
            sample_text = remove_markdown_formatting(st.session_state['reading_report'])
        elif st.session_state['active_report'] == 'recognition' and st.session_state.get('recog_eval_report'):
            st.markdown(st.session_state['recog_eval_report'])
            sample_text = remove_markdown_formatting(st.session_state['recog_eval_report'])
    except Exception as e:
        st.error(f"Error displaying report: {e}")
        sample_text = ""

# Buttons for switching between reports
col1, col2 = st.columns(2)
with col1:
    if st.button('Show Reading Report', use_container_width=True):
        st.session_state['active_report'] = 'reading'
        st.rerun()

with col2:
    if st.button('Show Image Identification Report', use_container_width=True):
        st.session_state['active_report'] = 'recognition'
        st.rerun()

# Text-to-speech buttons
btn_1, _, btn_3 = st.columns(3)
with btn_1:
    if st.button('Read out Report', use_container_width=True):    
        try:
            if sample_text:
                output_file = lg.text_to_wav(
                    voice_name='en-GB-Standard-A',
                    text=sample_text,
                    output_filename='speech'
                )
        except Exception as e:
            st.error(f"Error generating speech: {e}")

# Play audio
try:
    if os.path.exists('speech.wav'):
        st.audio('speech.wav', autoplay=False)
except Exception as e:
    pass

# Navigation buttons
bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Exercise', use_container_width=True):
        # Delete speech.wav if it exists
        try:
            if os.path.exists('speech.wav'):
                os.remove('speech.wav')
        except Exception as e:
            st.error(f"Error deleting speech file: {e}")
            
        # Clear session state
        st.session_state['reading_report'] = None
        st.session_state['recog_eval_report'] = None
        st.session_state['active_report'] = 'reading'  # Reset to default
        st.switch_page('pages/1_TakePhoto_btn.py')

with bt_3:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')