from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Define ChromaDB storage path
CHROMA_PATH = "chroma"

# Define prompt template
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

class RAGChatbot:
    def __init__(self):
        """Initialize ChromaDB and OpenAI Model"""
        self.embedding_function = OpenAIEmbeddings()
        self.db = Chroma(persist_directory=CHROMA_PATH, embedding_function=self.embedding_function)
        self.model = ChatOpenAI(model_name="gpt-3.5-turbo")  

    def query(self, query_text):
        """Retrieves relevant documents and generates a response"""
        results = self.db.similarity_search_with_relevance_scores(query_text, k=3)

        
        if len(results)==0 or results[0][1] < 0.7:
            response_text = self.model.invoke(query_text)
            
            #response_text = response.get("content", str(response))
            #print(f"When no response is found : {response_text}")
            return response_text.content,["ChatGPT knowledge"]

        
        
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)

        # Generate response from OpenAI
        response_text = self.model.invoke(prompt)
        #response_text = response.get("content", str(response))
        #print(f"When response is found : {response_text}")

        
        # Extract sources
        sources = [doc.metadata.get("source", None) for doc, _ in results]

        return response_text.content, sources

