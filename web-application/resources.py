# pages/resources.py
import streamlit as st

def resources_page():
    st.title('Resources')
    
    st.write("Here are some useful links related to this project:")
    
    st.markdown("""
    - [My Notebook](https://www.kaggle.com/code/charanchang/text-summarization)
    - [Project Repository](https://github.com/GaoWeiChang/Text-Summarization)
    - [Datasets](https://www.kaggle.com/datasets/nileshmalode1/samsum-dataset-text-summarization)
    """)
    