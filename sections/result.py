import streamlit as st

from .questions import reset
from .styling import load_result_css
from .chat.bot import create_answer


def parse_chat_prompt(questions, responses):
    prompt = ""
    for q_id, question in questions.items():
        prompt += question + "\n" + responses[q_id] + "\n\n"
    return prompt


def result_page():
    load_result_css()
    st.markdown("## Ergebnis")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("_Du bist noch nicht eingeloggt._")
        st.button("Zum Login")

    with col2:
        with st.spinner("Schreibe Post ..."):
            prompt = parse_chat_prompt(st.session_state.questions,
                                    st.session_state.responses)
            print(prompt)
            response = create_answer(prompt)
            st.text_area("Dein Post:", value=response, height=150,
                        key="text_to_copy",
                        help="Auswählen und kopieren oder den Button drücken.")
            st.markdown("___")

        if st.button("Neuer Post"):
            st.session_state.current_page = "questionnaire"
            reset()
            st.rerun()
