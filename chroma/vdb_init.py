from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import logging
import os
from docx import Document


logger = logging.getLogger(__name__)

v_db_path = os.path.join(os.getcwd(), "vdb")
if not os.path.exists(v_db_path):
    os.mkdir(v_db_path)


def init_openai_embeddings():
    embeddings_model = OpenAIEmbeddings(
        openai_api_key="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",
    )
    return embeddings_model


try:
    file_path = os.path.join(
        
        os.getcwd(),
        "media",
        "documents",
        "Accounts Receivable_INT4.1.docx",
        "Residence iEnabler INT 4.1.docx",

        
    )

    # Create a PyPDFLoader
    loader = Docx2txtLoader(file_path)

    # Load the PDF file
    documents = loader.load()

    # splitting the text into
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
    )
    texts = text_splitter.split_documents(documents)

    embeddings_model = init_openai_embeddings()

    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embeddings_model,
        persist_directory=v_db_path,
    )

    # persiste the db to disk
    vectordb.persist()
    print("vector database initializion is complete")
except Exception as e:
    print(f"An error occurred while initializing the database:\n{e}")

