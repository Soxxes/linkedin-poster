import streamlit as st


def load_question_css():
    st.markdown("""
        <style>
        /* EXAMPLES */
        /* Buttons */
        div.stButton > button:first-child {
            border: 2px solid #3557c0;
            background-color: #2b57df;
            width: 40%;
            margin: 0 auto;
                display: block;
        }

        /* Background gradient for the whole page */
        body, html {
            height: 100%;
            margin: 0;
        }
        .stApp {
            background-image: linear-gradient(to right, #00416A, #E4E5E6);
        }
        </style>
    """, unsafe_allow_html=True)


def load_result_css():
    st.markdown("""
        <style>
        /* EXAMPLES */
        /* Buttons */
        div.stButton > button:first-child {
            border: 2px solid #3557c0;
            background-color: #2b57df;
            width: 40%;
            margin: 0 auto;
                display: block;
        }

        /* Background gradient for the whole page */
        body, html {
            height: 100%;
            margin: 0;
        }
        .stApp {
            background-image: linear-gradient(to right, #00416A, #E4E5E6);
        }

        /* additional styling to ensure horizontal centering and a bit of formatting */
        .stMarkdown {
            text-align: center;
            margin: auto;
        }

        </style>
    """, unsafe_allow_html=True)
    