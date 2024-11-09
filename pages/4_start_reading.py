import base64
import streamlit as st
import logic as lg

st.set_page_config(
    page_title="Start Reading",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed")

# Create tabs
tab1, tab2, tab3 = st.tabs(["Reading And Comprehension", "Image and Object Identification", "Questions And Answer"])

# Content for Reading And Comprehension
with tab1:
    # Define header
    st.header("Reading And Comprehension")

    # Displays Uploaded Image
    st.write('')
    st.image('image_1.jpg', caption='Uploaded Image')
    st.write('')

    # Gets text from images
    image_text_reading = lg.text_from_image('image_1.jpg')
    
    # Takes Users passage reading
    audio_recording_1 = st.audio_input('read out passage')
    
    # Set condition for recording
    if audio_recording_1:
    
        # save audio
        try: 
            with open('audio_1.mp3', "wb") as f:
                f.write(audio_recording_1.getbuffer())
        except Exception as e:
            print(e)
        
        # Gets text from recording
        audio_text_reading = lg.text_from_audio('audio_1.mp3')
        
        # Display text from recording
        with st.container(border=True):
            st.subheader('Transcribed Audio')
            st.write(audio_text_reading)
    
        # Evaluate reading
        reading_eval_report = lg.evaluate_passage_reading(passage=image_text_reading, word=audio_text_reading)

        # Save in session state
        st.session_state['reading_report'] = reading_eval_report


# Content for Image and Object Identification
with tab2:
    
    # Gets text from images
    st.header("Image and Object Identification")
    
    # Displays Uploaded Image
    st.write('')
    st.image('image_1.jpg', caption='Uploaded Image')
    st.write('')
    
    # Identifies Image
    image_text_recog = lg.image_recognition('image_1.jpg')
    
    # Takes Users passage reading
    audio_recording_2 = st.audio_input('Identify image')
    
    # Set condition for recording
    if audio_recording_2:
    
        # save audio
        try: 
            with open('audio_1.mp3', "wb") as f:
                f.write(audio_recording_2.getbuffer())
        except Exception as e:
            print(e)
    
        # Gets text from recording
        audio_text_recog = lg.text_from_audio('audio_1.mp3')

        # Display text from recording
        with st.container(border=True):
            st.subheader('Transcribed Audio')
            st.write(audio_text_recog)
            
        # Evaluate reading
        recog_eval_report = lg.evaluate_image_recognition(response=audio_text_recog, observation=image_text_recog)

        # Save in session state
        st.session_state['recog_eval_report'] = recog_eval_report

# Content for Q/A
with tab3:
    # Sets header
    st.header('Q/A')

    # Set questions
    questions_reading = lg.set_questions(image_text_reading)

# Content for Q/A
with tab3:
    # Sets header
    # st.header('Q/A')

    # Set questions
    questions_reading = lg.set_questions(image_text_reading)
    # Display markdown
    st.markdown(questions_reading)


_ , bt_2, _ = st.columns(3)
with bt_2:
    if st.button('FeedBack', use_container_width=True):
        st.switch_page('pages/5_feedback.py')
