# Import required packages
import os
import pickle

from dotenv import load_dotenv
import streamlit as st

from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback

# Load environmental variables
load_dotenv()

# Main function
def main():
    st.image("logo.png")
    st.header("ASK QUESTIONS ABOUT YOUR PDF")

    # Upload a PDF file
    pdf = st.file_uploader("Upload your PDF", type='pdf')

    # If a PDF file is uploaded
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        # Extract text from the PDF file
        text = "".join(page.extract_text() for page in pdf_reader.pages)

        # Split the extracted text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
        chunks = text_splitter.split_text(text=text)

        # Define vector store name
        store_name = pdf.name[:-4]
        st.write(f'{store_name}')

        # If vector store exists, load it; otherwise, create a new one
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"pickles/{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"pickles/{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        # User input to ask questions about the uploaded PDF file
        query = st.text_input("Write your question and press ENTER.")

        # If a query is inputted
        if query:
            with st.spinner('Thinking...'):
                # Search for the most similar documents
                docs = VectorStore.similarity_search(query=query, k=3)

                # Initialize a language model and a question answering chain
                llm = OpenAI()
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    # Run the chain and get a response
                    response = chain.run(input_documents=docs, question=query)
                    print(cb)
                # Display the response
                st.write(response)

# Run the main function
if __name__ == '__main__':
    main()
