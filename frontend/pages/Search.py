import streamlit as st
import requests

from config import API_URL
from components.navbar import show_navbar
from components.sidebar import show_sidebar

st.set_page_config(
    page_title="Search Movies",
    page_icon="",
    layout="wide"
)

show_sidebar()
show_navbar()

st.title(" Search Movies")

st.write("Search any movie available in the recommendation dataset.")

movie_name = st.text_input(
    "Movie Name",
    placeholder="Example: Avatar"
)

if movie_name:

    try:

        response = requests.get(
            f"{API_URL}/search",
            params={"movie": movie_name}
        )

        movies = response.json()

        if len(movies) == 0:

            st.warning("No movie found.")

        else:

            st.success(f"{len(movies)} movie(s) found")

            cols = st.columns(2)

            for index, movie in enumerate(movies):

                with cols[index % 2]:

                    st.markdown(
                        f"""
                        <div style="
                            background:#181818;
                            padding:15px;
                            border-radius:10px;
                            margin-bottom:15px;
                            border:1px solid #333;
                        ">
                            <h4 style="color:white;">
                                 {movie}
                            </h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    except Exception as e:

        st.error(f"Unable to connect to Flask API.\n\n{e}")