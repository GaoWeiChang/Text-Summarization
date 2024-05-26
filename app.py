import streamlit as st

# Tab name and icon
st.set_page_config(
    page_title="Text Summarizer", 
    page_icon="📝",  
)
from summarize import summarize_page
from resources import resources_page

# myenv\Scripts\activate 
# streamlit run app.py

# for execute 
page = st.sidebar.selectbox('Navigate', ("Summarize", "Resources"))

if page == "Summarize":
    summarize_page()
elif page == "Resources":
    resources_page()