#Import Necessary Modules

from dotenv import load_dotenv
import os
from langchain.llms import GooglePalm
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import CSVLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Take environment variables from .env (especially the Google API key)
load_dotenv()

#Create Google Palm LLM model
llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0)

#Initialize instructor embeddings using the Hugging Face model
embeddings = HuggingFaceInstructEmbeddings()
Vector_Path = "New_Faiss_Index"

def create_vector():
    try:

        # Load data from Dataset
        loader = CSVLoader(file_path='/Users/rafaelzieganpalg/Programming/LangChain_Project/Rafael_QA/Stan_Data_UPG.csv',source_column='question')
        data = loader.load()
    
        # Create a FAISS instance for vector database from 'data'
        Vector_db=FAISS.from_documents(documents=data, embedding=embeddings)

        # Save vector database locally
        Vector_db.save_local(Vector_Path)
    except Exception as e:
        print(f"An error occurred while creating the vector database: {e}")


def get_qa_chain():
     try:
         
        # Load the vector database from the local folder
        Vector_db = FAISS.load_local(Vector_Path,embeddings,allow_dangerous_deserialization=True)

        # Create a retriever for querying the vector database
        retriever = Vector_db.as_retriever()

        prompt_template = """Given the following context and a question, generate an answer based on this context only.
                            In the answer try to provide as much text as possible from "response" section in the source 
                            document context without making much changes.If the answer is not found in the context, 
                            kindly state "I don't know." Don't try to make up an answer.
                            CONTEXT: {context}
                            QUESTION: {question}"""
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        chain_type_kwargs = {"prompt": PROMPT}
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            input_key="query",
            return_source_documents= True,
            chain_type_kwargs= chain_type_kwargs
            )
        return chain
     except Exception as e:
        print(f"An error occurred while getting the QA chain: {e}")


    

if __name__ == "__main__":
    chain = get_qa_chain()
    if chain:
        print(chain("Who is Beyonce"))
