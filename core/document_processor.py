from typing import List
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import settings


class DocumentProcessor:
    
    def __init__(self,chunk_size:int=None,chunk_overlap:int=None):
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap
        
        self.text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            separators=["\n\n","\n"," ",""],
        )
    
    def load_document(self,file_path:str)->List[Document]:
        path=Path(file_path)
        extension=path.suffix.lower()
        if extension==".txt":
            loader=TextLoader(file_path,encoding="utf-8")
        elif extension==".pdf":
            loader=PyPDFLoader(file_path)
        else:
            raise ValueError(f" Unsupported file {extension}. Use .txt or .pdf ")
        return loader.load()
    
    def load_from_text(self,text:str,metadata:dict=None)->List[Document]:
        
         metadata=metadata or {}
         return [Document(page_content=text,metadata=metadata)]
     
    
    def split_documents(self,documents:List[Document])->List[Document]:
        
        """
        Split documents into smaller chunks,
        Args:
        documents:List of Document object
        """
        return self.text_splitter.split_documents(documents)
        
    def process(self,file_path:str)->List[Document]:
        """
        complete pipeline:load and split into smaller documents/chunks
        Args:
        file path:Path to a document file
        """
        documents=self.load_document(file_path)
        
        # split into chunks 
        chunks=self.split_documents(documents)
        return chunks
    
    
        
