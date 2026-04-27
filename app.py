import streamlit as st

st.set_page_config(page_title="Redirecting...", page_icon="🔄")

st.markdown(
    """
    <meta http-equiv="refresh" content="0; url=https://northstar.streamlit.app">
    <script>window.location.replace("https://northstar.streamlit.app");</script>
    """,
    unsafe_allow_html=True,
)

st.markdown("Redirecting to [northstar.streamlit.app](https://northstar.streamlit.app)...")
