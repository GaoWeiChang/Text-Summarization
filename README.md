# Text Summarization with LLM
## Overview
&nbsp;&nbsp;&nbsp;&nbsp;This project we will use a pre-trained Large Language Model (LLM) to perform text summarization.
The summarization can be described as the creation of a shorter version of a document or an article that captures all the important information. After we trained the model, we will create user interface allow to
interact with, we will build [web application](https://text-summarization-jyfdhmbyhnvcvdkhgzxnh4.streamlit.app/) by using Streamlit, providing an interactive and user-friendly interface for users to input text and receive concise summaries. It supports a variety of text types, including chats, news articles, and more.

## Features
&nbsp;&nbsp;&nbsp;&nbsp;Interactive Interface: User-friendly web application built with Streamlit.
Variety of Text Types: Handles different types of text such as chat messages, news articles, and more.
Real-Time Processing: Fast and efficient text summarization.
Time Saved: Allow you to understanding the main ideas of the long article in short time.

## Method

1. **Use the Samsum Dataset for Text Summarization**:
   - The Samsum dataset from [Kaggle](https://www.kaggle.com/datasets/nileshmalode1/samsum-dataset-text-summarization) is utilized for fine-tuning the pre-trained LLM.

2. **Explore and Preprocess Data**:
   - Explore the dataset to understand its structure and content.
   - Preprocess the data to clean and prepare it for model training.

3. **Tokenize and Embed the Text Data**:
   - Tokenize the text data and generate embeddings to prepare it for fine-tuning.

4. **Fine-tune the T5 Model**:
   - Use the T5 model from Huggingface and fine-tune it on the prepared dataset.

5. **Create a Pipeline**:
   - Develop a pipeline to easily invoke the fine-tuned model for summarization tasks.

6. **Create Web App UI with Streamlit**:
   - Build a user-friendly web application interface using Streamlit.
   - Integrate the pipeline into the Streamlit app to enable text summarization.

7. **Deploy the Streamlit App**:
   - Deploy the finished Streamlit app to make it accessible to users.

## Technologies Used
   - Streamlit: Web framework for creating interactive web applications.
   - Huggingface Transformers: Library for pre-trained language models.
   - Python: Programming language and Libraries.
   - Kaggle: Source for the Samsum dataset.
