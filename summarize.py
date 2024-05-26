# pages/summarize.py
import streamlit as st
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

@st.cache_resource
def load_model():
    repo = "gaoweic/Model"
    saved_model = AutoModelForSeq2SeqLM.from_pretrained(repo)
    saved_tokenizer = AutoTokenizer.from_pretrained(repo)

    return saved_model, saved_tokenizer

def summarize_page ():
    st.title('Text Summarizer')
    
    # Input text
    text = st.text_area('Enter text to summarize', height=200)
    
    # Create the summarization pipeline
    saved_model, saved_tokenizer = load_model()
    summarizer = pipeline('summarization', model=saved_model, tokenizer=saved_tokenizer)

    # Summarize button
    if st.button('Summarize'):
        if text:
            # Perform summarization
            summary = summarizer(text, max_length=300, min_length=20, do_sample=False)
            # Display summary
            st.subheader('Summary')
            st.write(summary[0]['summary_text'])
        else:
            st.write('Please enter some text to summarize.')
