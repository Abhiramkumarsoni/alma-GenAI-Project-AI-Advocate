
from langchain_core.documents import Document
from core.embeddings import EmbeddingManager
from core.vector_store import VectorStoreManager
from core.chain import RAGChain
from tools.tavily_search import TavilySearchTool

import os

def main():
    print("\n" + "=" * 70)
    print("🎓  RAG Chain & Web Search Demo")
    print("=" * 70)
    
    # Step 1: Create sample knowledge base
    print("\n📚 Step 1: Creating knowledge base...")
    sample_docs = [
        Document(
            page_content="Python is a high-level programming language created by Guido van Rossum in 1991. "
                        "It emphasizes code readability and has a comprehensive standard library.",
            metadata={"source": "python_intro.txt"}
        ),
        Document(
            page_content="Machine learning is a subset of artificial intelligence that enables systems to learn "
                        "and improve from experience without being explicitly programmed.",
            metadata={"source": "ml_basics.txt"}
        ),
        Document(
            page_content="Deep learning uses artificial neural networks with multiple layers to process data "
                        "and is particularly effective for image recognition and natural language processing.",
            metadata={"source": "deep_learning.txt"}
        ),
        Document(
            page_content="LangChain is a framework for developing applications powered by language models. "
                        "It enables data connection, agent logic, and integration with various tools.",
            metadata={"source": "langchain_overview.txt"}
        ),
    ]
    print(f"Created {len(sample_docs)} documents")
    
    print(f"Step 2: Setting up vector store")
    
    embedder=EmbeddingManager()
    vs_manager=VectorStoreManager(embedder)
    vs_manager.create_from_documents(sample_docs)
    print(f"Vector strored created and indexed")
    
    # STEP 3: Created RAG chain
    print("\n Step 3: Intializing RAG chain...")
    
    rag=RAGChain(vs_manager)
    
    print(f"Rag chain is ready")
    print(f"LLM model:{rag.model_name}")
    print("\n📄 Step 4: Testing document-only queries...")
    doc_queries = [
        "What is Python?",
        "Explain machine learning",
        "What is LangChain?"
    ]
    
    for i, query in enumerate(doc_queries, 1):
        print(f"\n   Query {i}: '{query}'")
        result = rag.query(query)
        print(f"   Answer: {result['answer'][:150]}...")
        print(f"   Sources: {result['sources']}")
    
    # Step 5: Test web search tool
    print("\n🌐 Step 5: Testing web search tool...")
    search_tool = TavilySearchTool(max_results=3)
    print("✅ Tavily search tool initialized")
    print("   (Ready to search: 'NVIDIA stock price', 'Latest AI news', etc.)")
    response= search_tool.search("What is Nvidia current AI news")
    print(response)
    
    
    