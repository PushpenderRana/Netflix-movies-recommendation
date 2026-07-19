import streamlit as st

from config import APP_NAME, PAGE_ICON, LAYOUT
from services.api import get_movies, recommend_movie
from components.navbar import show_navbar
from components.sidebar import show_sidebar
from components.movie_card import movie_card

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# ----------------------------------
# Load CSS
# ----------------------------------

try:
    with open("assets/style.css", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass

# ----------------------------------
# Sidebar & Navbar
# ----------------------------------

show_sidebar()
show_navbar()

# ----------------------------------
# Hero Section
# ----------------------------------

st.markdown(
    """
# 🍿 Discover Your Next Favorite Movie

Get instant movie recommendations using an AI-powered
content-based recommendation engine.
"""
)

st.divider()

# ----------------------------------
# Load Movies
# ----------------------------------

with st.spinner("Loading movies..."):
    movies = get_movies()

if not movies:
    st.error("❌ Unable to connect to Flask API.")
    st.stop()

# ----------------------------------
# Movie Selection
# ----------------------------------

col1, col2 = st.columns([4, 1])

with col1:

    selected_movie = st.selectbox(
        "🎬 Select a Movie",
        movies,
        index=None,
        placeholder="Search movie..."
    )

with col2:

    st.write("")
    st.write("")
    recommend = st.button(
        "Recommend",
        use_container_width=True
    )

# ----------------------------------
# Recommendation
# ----------------------------------

if recommend:

    if not selected_movie:

        st.warning("Please select a movie first.")

    else:

        with st.spinner("Finding similar movies..."):

            result = recommend_movie(selected_movie)

        if result.get("success"):

            st.divider()

            st.subheader(
                f"🎯 Because you liked **{selected_movie}**"
            )

            st.write("You may also enjoy these movies:")

            cols = st.columns(5)

            for i, movie in enumerate(result["recommendations"]):

                with cols[i]:
                   
                    movie_card(movie)

        else:

            st.error(result.get("message", "Movie not found."))

# ----------------------------------
# Footer
# ----------------------------------

st.divider()

st.caption(
    "Built with ❤️ using Flask, Streamlit, Scikit-Learn & Pandas"
)