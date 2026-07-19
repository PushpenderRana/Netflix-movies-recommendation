import streamlit as st


def show_sidebar():

    with st.sidebar:

        # -----------------------------
        # Logo
        # -----------------------------
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/7/75/Netflix_icon.svg",
            width=90
        )

        st.markdown(
            "<h1 style='color:white;'>Netflix AI</h1>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        # -----------------------------
        # Recommendation
        # -----------------------------
        st.markdown(
            "<h3 style='color:white;'>🎬 Recommendation</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                background:#1E1E1E;
                padding:12px;
                border-radius:10px;
                border-left:5px solid #E50914;
                color:white;
                font-weight:bold;
                margin-bottom:15px;
            ">
                🎯 Content-Based Filtering
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        # -----------------------------
        # Tech Stack
        # -----------------------------
        st.markdown(
            "<h3 style='color:white;'>🛠 Tech Stack</h3>",
            unsafe_allow_html=True
        )

        st.markdown("""
- 🐍 **Python**
- 🌐 **Flask API**
- 🎨 **Streamlit**
- 🤖 **Scikit-Learn**
- 🐼 **Pandas**
- 📦 **Pickle**
        """)

        st.markdown("---")

        # -----------------------------
        # Developer
        # -----------------------------
        st.markdown(
            "<h3 style='color:white;'>👨‍💻 Developer</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                background:#1E1E1E;
                padding:12px;
                border-radius:10px;
                border-left:5px solid #E50914;
                color:white;
                font-weight:bold;
                text-align:center;
            ">
                Pushpender Rana
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        # -----------------------------
        # Footer
        # -----------------------------
        st.caption("© 2026 Netflix Recommendation System")