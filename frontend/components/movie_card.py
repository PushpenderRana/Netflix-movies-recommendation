import streamlit as st


def movie_card(movie):

    title = movie["title"]
    rating = movie["vote_average"]
    release = movie["release_date"][:4]
    runtime = movie["runtime"]
    tagline = movie.get("tagline", "")

    genres = str(movie["genres"])
    if genres.startswith("["):
        genres = genres.strip("[]")
        genres = genres.replace("'", "")
        genres = genres.replace(",", " •")

    overview = movie["overview"]

    preview = overview[:180] + "..." if len(overview) > 180 else overview

    with st.container(border=True):

        st.markdown(f"###  {title}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f" **{rating}**")
            st.markdown(f" **{release}**")

        with col2:
            st.markdown(f" **{runtime} min**")

        st.markdown(f" **{genres}**")

        if tagline:
            st.caption(f"*{tagline}*")

        

        with st.expander(" Read More"):
            st.write(overview)