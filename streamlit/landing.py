import streamlit as st
st.set_page_config(page_title="My Streamlit App", page_icon=":guardsman:")

st.markdown("""
    <link rel="stylesheet" href="styles.css">
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header">
        <img src="logo.png" alt="Logo">
        <button>Try for FREE</button>
    </div>
""", unsafe_allow_html=True)

st.video("video.mp4",start_time=10)

st.markdown("""
    <p>Welcome to my Streamlit App!</p>
""", unsafe_allow_html=True)

if st.sidebar.button("About"):
    st.write("About page")
if st.sidebar.button("Problem"):
    st.write("Problem page")
if st.sidebar.button("Solution"):
    st.write("Solution page")
if st.sidebar.button("Feedback"):
    st.write("Feedback page")
if st.sidebar.button("Contact"):
    st.write("Contact page")
