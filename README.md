# Question Answering System with FAISS and Hugging Face Models


![image](https://github.com/Neerajjv/LLM-Project-End-to-End-LLM-Project-Using-LangChain-Google-Palm/assets/154986859/3eb1d776-d902-43c7-b79a-c3be744337f9)# LLM-Project-End-to-End-LLM-Project-Using-LangChain-Google-Palm

This repository contains code for an end-to-end question-answering system built using LangChain, Google Palm LLM (Large Language Model), FAISS (Facebook AI Similarity Search) and Vector bases

## Overview

The project is an end-to-end question-answering system leveraging LangChain for document loading, Google Palm LLM for language understanding, FAISS for vector indexing, and Hugging Face's pre-trained models for efficient retrieval of answers from a dataset.

## LM Project | End to End LLM Project Using LangChain, Google Palm

This project is an example of an end-to-end language model (LLM) project that incorporates LangChain for document loading, Google Palm LLM for language understanding, and FAISS for vector indexing. It demonstrates the process of creating a question-answering system from scratch using standard tools and techniques.



## Features

- Create a vector database from a CSV dataset containing questions and answers.
- Retrieve answers from the vector database based on user queries.
- Utilize Hugging Face's pre-trained models for language embeddings.
- Handle cases where the answer is not found in the dataset gracefully.

## Usage

1. Prepare your dataset:
   - Ensure your dataset is in CSV format with columns "Question" and "Answer".
   - Save your dataset as `data.csv` in the project directory.

2. Run the script to create the vector database:
   ```bash
   python helper.py
3. streamlit run Main.py
