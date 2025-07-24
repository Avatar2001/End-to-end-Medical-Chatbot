from src.helpers import load_pdf_data,split_data,download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()  

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY is missing from environment variables")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY  

extracted_data = load_pdf_data('data/')

text_chunks=split_data(extracted_data)
embeddings=download_hugging_face_embeddings()

pc=pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-chatbot-index"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1",
    )
)
#embed each chunk and upsert the embedding into your pinecone index
docsearch=PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)
