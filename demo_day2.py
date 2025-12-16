"""
Demo Script - Day 2: Embeddings & Vector Store
===============================================
This script demonstrates creating embeddings and building a vector store.

Run with: python demo_day2.py
"""

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from core.document_processor import DocumentProcessor
from core.embeddings import EmbeddingManager
from core.vector_store import VectorStoreManager


def main():
    print("\n" + "=" * 70)
    print("🎓 DAY 2 DEMO: Embeddings & Vector Store")
    print("=" * 70)
    
    # Create sample document
    print("\n📝 Step 1: Creating sample documents...")
    sample_content = """
    Python is a high-level programming language for web development and data science.
    Machine learning is a subset of artificial intelligence that enables computers to learn.
    Deep learning uses neural networks with multiple layers for complex pattern recognition.
    Data science combines statistics, programming, and domain knowledge for insights.
    Natural language processing helps computers understand and generate human language.
    """
    
    with open("sample.txt", "w") as f:
        f.write(sample_content)
    
    print("✅ Created sample document")
    
    # Step 2: Process documents
    print("\n📄 Step 2: Processing documents...")
    processor = DocumentProcessor(chunk_size=150, chunk_overlap=30)
    chunks = processor.process("sample.txt")
    print(f"✅ Split into {len(chunks)} chunks")
    
    # Step 3: Create embeddings
    print("\n🔢 Step 3: Creating embeddings...")
    print("   (Downloading model on first run - this may take a minute...)")
    embedder = EmbeddingManager()
    print("✅ Embedding model loaded")
    print(f"   Model: {embedder.model_name}")
    print(f"   Dimension: {embedder.get_embedding_dimension()}")
    
    # Step 4: Build vector store
    print("\n📊 Step 4: Building vector store...")
    vs_manager = VectorStoreManager(embedder)
    vs_manager.create_from_documents(chunks)
    print(f"✅ Vector store created with {len(chunks)} documents")
    
    # Step 5: Test semantic search
    print("\n🔍 Step 5: Testing semantic search...")
    test_queries = [
        "What is Python used for?",
        "How does machine learning work?",
        "Tell me about neural networks",
        "What is data science?"
    ]
    
    for query in test_queries:
        print(f"\n   Query: '{query}'")
        results = vs_manager.search(query, k=2)
        for i, doc in enumerate(results, 1):
            print(f"   {i}. {doc.page_content[:60]}...")
    
    # Step 6: Save vector store
    print("\n💾 Step 6: Saving vector store...")
    vs_manager.save()
    print(f"✅ Vector store saved to {vs_manager.index_path}/")
    
    # Step 7: Load and verify
    print("\n📂 Step 7: Loading saved vector store...")
    vs_loader = VectorStoreManager(embedder)
    vs_loader.load()
    print("✅ Vector store loaded successfully")
    
    # Verify it works
    test_result = vs_loader.search("Python programming", k=1)
    print(f"✅ Verification search returned: {test_result[0].page_content[:50]}...")
    
    # Statistics
    print("\n" + "=" * 70)
    print("📊 STATISTICS")
    print("=" * 70)
    print(f"Documents indexed: {len(chunks)}")
    print(f"Embedding dimension: {embedder.get_embedding_dimension()}")
    print(f"Vector store location: {vs_manager.index_path}")
    
    # Cleanup
    os.remove("sample.txt")
    print("\n✅ Cleaned up temporary files")
    
    print("\n" + "=" * 70)
    print("🎉 DAY 2 DEMO COMPLETE!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("✓ Embeddings convert text into semantic vectors")
    print("✓ FAISS enables fast similarity search")
    print("✓ Vector stores can be persisted and reloaded")
    print("✓ Semantic search finds contextually similar documents")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()