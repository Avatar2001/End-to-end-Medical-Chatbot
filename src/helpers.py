from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


#extract data from pdf files
def load_pdf_data(file_path):
    loader=DirectoryLoader(file_path,glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents


#split data into chunks
def split_data(extracted_documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_documents = text_splitter.split_documents(extracted_documents)
    return split_documents

#download embeddings from hugging face
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings