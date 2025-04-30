# 🤖 RAG-IT Chatbot (GPT-3.5 + LangChain)

A production-level **IT Support Chatbot** built using **Retrieval-Augmented Generation (RAG)**, **OpenAI’s GPT-3.5**, and **LangChain**. This project enables intelligent, context-aware question answering based on internal knowledge documents, providing fast and accurate tech support solutions.

---

## 🧠 Key Features

- 🗂️ **Contextual QA via RAG**: Combines LLM reasoning with document retrieval  
- 🔍 **Semantic Search**: Finds relevant IT support docs using vector similarity  
- 🧑‍💻 **Interactive Chat Interface**: Real-time conversations powered by GPT-3.5  
- 🏗️ **Modular LangChain Architecture**: Easily extendible with new tools or APIs  
- 🛡️ **Private Knowledge Base**: Keeps internal data secure and queryable

---

## 🔧 Tech Stack

- **LLM Backend**: OpenAI GPT-3.5
- **Framework**: LangChain
- **Vector Store**: FAISS / ChromaDB
- **Embedding Model**: OpenAI or HuggingFace Transformers
- **Frontend**: Streamlit (optional)
- **Utilities**: dotenv, tiktoken, PyMuPDF, Python

---

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a .env file in the root directory with the following:
```bash
OPENAI_API_KEY=your_openai_key
```

### 4. Ingest Knowledge Base
```bash
python ingest.py
```
This step processes documents in /data and builds the vector index.

### 5. Launch the Chatbot
```bash
python langchain_app.py
```

