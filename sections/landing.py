import streamlit as st


def landing_page():
    st.title("Mein LinkedIn Post Schreiber")
    st.markdown("### Top-informierte KI für bessere Posts")
    if st.button("Okay, los geht's"):
        st.session_state.current_page = "questionnaire"
        st.rerun()
