import streamlit as st

from components.navbar import show_navbar
from components.sidebar import show_sidebar

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

show_sidebar()

show_navbar()

st.title("ℹ️ About Project")

st.markdown("---")

st.header("Project Overview")

st.write("""
This project is an AI-powered Movie Recommendation System
that recommends movies similar to the one selected by the user.

The recommendation engine is built using
Content-Based Filtering with Cosine Similarity.
""")

st.markdown("---")

st.header("Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Backend")

    st.write("""
- Flask
- Python
- Pandas
- Scikit-Learn
- Pickle
""")

with col2:

    st.subheader("Frontend")

    st.write("""
- Streamlit
- Requests
- HTML/CSS
""")

st.markdown("---")

st.header("Recommendation Algorithm")

st.write("""
✔ Data Cleaning

✔ Feature Engineering

✔ TF-IDF / Tags

✔ Cosine Similarity

✔ Top 5 Similar Movies
""")

st.markdown("---")

st.header("API Endpoints")

st.code("""
GET     /
GET     /movies
GET     /search
POST    /recommend
""")

st.markdown("---")

st.success("Developed by Pushpender Rana")