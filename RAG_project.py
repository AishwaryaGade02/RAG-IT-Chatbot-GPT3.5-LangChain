import pandas as pd

data = pd.read_csv("data/rag_sample_qas_from_kis.csv") 
data.head()

text_list = [f"Q: {q}\nA: {a}" for q, a in zip(data["ki_topic"], data["sample_ground_truth"])]

# Save to a Markdown (.md) file
with open("dataset.md", "w", encoding="utf-8") as f:
    f.write("\n\n".join(text_list))

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

CHROMA_PATH = "chroma"

#DATA_PATH = os.path.join(os.getcwd())
Data_path = "dataset.md"

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def split_text(documents:list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function = len,
        add_start_index=True,

    )
    chunks = text_splitter.split_documents(documents)
    document = chunks[10]
    #print(f"This is from split_text function : {document}")

    return chunks

def save_to_chroma(chunks:list[Document]):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks,OpenAIEmbeddings(),persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)}")

def load_documents():
    #loader = DirectoryLoader(DATA_PATH, glob="*.md")
    loader = TextLoader(Data_path)
    documents = loader.load()
    print(f"This is from load function : {documents}")
    return documents

if __name__ == "__main__":
    main()
