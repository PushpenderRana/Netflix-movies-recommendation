import streamlit as st

def show_navbar():

    st.markdown(
        """
        <div style="
            background-color:#111111;
            padding:20px;
            border-radius:15px;
            border:1px solid #333;
            margin-bottom:25px;
        ">

        <h1 style="
            color:#E50914;
            text-align:center;
            margin-bottom:5px;
        ">
             Netflix Recommendation System
        </h1>

        <p style="
            color:#B3B3B3;
            text-align:center;
            font-size:18px;
            margin:0;
        ">
            AI Powered Movie Recommendation Engine
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )