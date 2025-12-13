"""
Demo Script - Day 1: Document Processing
==========================================
This script demonstrates loading and chunking documents.

Run with: python demo_day1.py
"""

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from pathlib import Path
from core.document_processor import DocumentProcessor


def main():
    print("\n" + "=" * 70)
    print("🎓 DAY 1 DEMO: Document Processing & Chunking")
    print("=" * 70)
    
    # Create sample document
    print("\n📝 Step 1: Creating sample document...")
    sample_content = """
    Python is a high-level programming language known for its simplicity and readability.
    It was created by Guido van Rossum and released in 1991.
    
    Python is widely used in various fields:
    1. Web Development - Django, Flask frameworks
    2. Data Science - Pandas, NumPy, Scikit-learn
    3. Machine Learning - TensorFlow, PyTorch
    4. Automation - Scripts and tools
    5. Scientific Computing - Research and analysis
    
    The language emphasizes code readability and allows developers to express concepts
    in fewer lines of code than would be possible in languages such as C++ or Java.
    
    Python's philosophy is embedded in the document called "The Zen of Python".
    Some key principles include:
    - Beautiful is better than ugly
    - Explicit is better than implicit
    - Simple is better than complex
    - Readability counts
    
    Python has a comprehensive standard library, often described as "batteries included".
    This means developers can find modules for most tasks without external dependencies.
    """
    
    with open("sample_document.txt", "w") as f:
        f.write(sample_content)
    
    print("✅ Created 'sample_document.txt'")
    
    # Initialize processor
    print("\n📄 Step 2: Initializing Document Processor...")
    processor = DocumentProcessor(chunk_size=300, chunk_overlap=50)
    print("✅ Processor configured (chunk_size=300, overlap=50)")
    
    # Process document
    print("\n⚙️  Step 3: Processing document...")
    chunks = processor.process("sample_document.txt")
    print(f"✅ Document split into {len(chunks)} chunks")
    
    # Display chunks
    print("\n📋 Step 4: Displaying chunks...")
    for i, chunk in enumerate(chunks, 1):
        print(f"\n--- CHUNK {i} ---")
        print(f"Content: {chunk.page_content[:150]}...")
        print(f"Length: {len(chunk.page_content)} chars")
        print(f"Metadata: {chunk.metadata}")
    
    # Statistics
    print("\n" + "=" * 70)
    print("📊 STATISTICS")
    print("=" * 70)
    total_chars = sum(len(chunk.page_content) for chunk in chunks)
    print(f"Total chunks: {len(chunks)}")
    print(f"Total characters: {total_chars}")
    print(f"Avg chunk size: {total_chars // len(chunks)} chars")
    print(f"Original content size: {len(sample_content)} chars")
    
    # Cleanup
    os.remove("sample_document.txt")
    print("\n✅ Cleaned up temporary file")
    
    print("\n" + "=" * 70)
    print("🎉 DAY 1 DEMO COMPLETE!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("✓ Documents are loaded from various file types")
    print("✓ Documents are split into meaningful chunks")
    print("✓ Chunks preserve context through overlap")
    print("✓ Metadata tracks document sources")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()