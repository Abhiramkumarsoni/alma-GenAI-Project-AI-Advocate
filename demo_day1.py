
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
    with open("sample_document.txt","w") as f:
        f.write(sample_content)
    
    print("create 'sample_document.txt")
    
    print("Initialize document processor")
    processor=DocumentProcessor(chunk_size=300,chunk_overlap=50)
    print("Process configured (chunk_size=300,chunk_overlap=50)")
    print("\n... Processing document")
    chunks=processor.process("sample_document.txt")
    print(f"document split into {len(chunks)} chunks")
    
    
    print("\n Displaying chunks...")
    for i,chunk in enumerate(chunks,1):
        print(f"\n-- chunk {i} ")
        print(f"Content {chunk.page_content[:150]}...")
        print(f"Length :{len(chunk.page_content)}")
        print(f"Metadata:{chunk.metadata}")


if __name__=="__main__":
    main()
    
    
    
    
    
    