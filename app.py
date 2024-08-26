import streamlit as st

from sections.landing import landing_page
from sections.questions import questionnaire_page
from sections.result import result_page


if 'current_page' not in st.session_state:
    st.session_state.current_page = "landing"
if 'current_group_index' not in st.session_state:
    st.session_state.current_group_index = 1
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# page routing
if st.session_state.current_page == "landing":
    landing_page()
elif st.session_state.current_page == "questionnaire":
    questionnaire_page()
elif st.session_state.current_page == "results":
    result_page()
