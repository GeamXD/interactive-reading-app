import streamlit as st


st.set_page_config(
    page_title="FeedBack",
    page_icon=":material/comment:",
    layout="centered",
    initial_sidebar_state="collapsed")

st.title('Feedback')
st.caption('Provide feedback on the accuracy of the spoken text.')

    
with st.container(border=True):
    try:
        if st.session_state['reading_report']:
            st.markdown(st.session_state['reading_report'])
            sample_text_1 = st.session_state['reading_report']
        if st.session_state['recog_eval_report']:
            st.markdown(st.session_state['recog_eval_report'])
            sample_text_2 = st.session_state['recog_eval_report']

    except:
        pass


btn_1, _,  btn_3= st.columns(3)
with btn_1:
    if st.button('Read out Reading Report', use_container_width=True):    
        # Convert text to speech
        try:
            output_file = lg.text_to_wav(
                voice_name='en-GB-Standard-A',
                text=sample_text_1,
                output_filename='speech'
            )
            st.success(f"Successfully generated audio file: {output_file}")
        except Exception as e:
            print(f"Error generating speech: {e}")

with btn_3:
    if st.button('Read out Image Identification Report', use_container_width=True):    
        # Convert text to speech
        try:
            output_file = lg.text_to_wav(
                voice_name='en-GB-Standard-A',
                text=sample_text_2,
                output_filename='speech'
            )
            st.success(f"Successfully generated audio file: {output_file}")
        except Exception as e:
            print(f"Error generating speech: {e}")

# Play audio
try:
    st.audio('speech.wav', autoplay=True)
except Exception as e:
    pass

bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Exercise', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')
with bt_3:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')