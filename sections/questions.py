from collections import defaultdict

import streamlit as st
import yaml

from .styling import load_question_css


# load questions from a YAML file and group them
def load_questions(filepath="sections/questions.yaml"):
    with open(filepath, 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)
    grouped_questions = defaultdict(list)
    for question in data['questions']:
        grouped_questions[question['group']].append(question)
    return grouped_questions

# based on the type of question we need to render it differently
def render_question(question):
    q_type = question['type']
    q_id = question['id']
    if q_type == 'text':
        response = st.text_input(question['question'], key=q_id)
    elif q_type == 'number':
        response = st.number_input(question['question'], key=q_id)
    elif q_type == 'radio':
        response = st.radio(question['question'], question['options'], key=q_id)
    return response

def reset():
    st.session_state.current_group_index = 1
    st.session_state.responses = {}


def questionnaire_page():
    load_question_css()
    if 'current_group_index' not in st.session_state:
        st.session_state.current_group_index = 1

    if 'responses' not in st.session_state:
        st.session_state.responses = {}

    if 'questions' not in st.session_state:
        st.session_state.questions = {}

    grouped_questions = load_questions()

    col1, col2 = st.columns(2)

    # Column 1: Placeholder for Image and Button
    with col1:
        st.image("./imgs/linkedin_logo.webp", use_column_width=True)
        if st.button("Neustart"):
            st.session_state.current_group_index = 1
            st.rerun()

    # Column 2: Render questions of the current group
    current_group_index = st.session_state.current_group_index
    with col2:
        if current_group_index in grouped_questions:
            for question in grouped_questions[current_group_index]:
                response = render_question(question)
                st.session_state.responses[question['id']] = response
                st.session_state.questions[question['id']] = question["question"]
        
        # Navigation buttons
        if st.button('Zurück', key="back") and current_group_index > 1:
            st.session_state.current_group_index -= 1
            st.rerun()
        if st.button('Weiter', key="next"):
            if current_group_index < max(grouped_questions.keys()):
                st.session_state.current_group_index += 1
                st.rerun()
            else:
                st.session_state.current_page = "results"
                st.rerun()
                