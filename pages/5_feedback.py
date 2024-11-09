import streamlit as st


st.set_page_config(
    page_title="FeedBack",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed")

st.title('Feedback')
st.caption('Provide feedback on the accuracy of the spoken text.')

    
with st.container(border=True):
    try:
        if st.session_state['reading_report']:
            st.markdown(st.session_state['reading_report'])
        if st.session_state['recog_eval_report']:
            st.markdown(st.session_state['recog_eval_report'])
    except:
        pass


_, btn_2, _ = st.columns(3)
with btn_2:
    if st.button('Read out Report', use_container_width=True):
        pass


bt_1, bt_2, bt_3 = st.columns(3)
with bt_1:
    if st.button('Retake Exercise', use_container_width=True):
        st.switch_page('pages/4_start_reading.py')
with bt_3:
    if st.button('Go to Overview', use_container_width=True):
        st.switch_page('pages/3_overview.py')