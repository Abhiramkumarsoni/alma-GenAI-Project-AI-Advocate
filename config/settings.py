

import os 
from dataclasses import dataclass

@dataclass
class Settings:
    

    GROQ_API_KEY:str =os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY:str =os.getenv("TAVILY_API_KEY")
    LLM_MODEL:str =os.getenv("LLM_MODEL")
    LLM_TEMPERATURE:float =os.getenv("LLM_TEMPERATURE")
    EMBEDDING_MODEL:str =os.getenv("EMBEDDING_MODEL")
    CHUNK_SIZE:int =os.getenv("CHUNK_SIZE")
    CHUNK_OVERLAP:int=os.getenv("CHUNK_OVERLAP")
    FAST_INDEX_PATH:str=os.getenv("FAST_INDEX_PATH")
    TOP_K_RESULT:str=os.getenv("TOP_K_RESULT")
    
    def validate(self)->bool:
        """Check if required API key are set"""
        if not self.GROQ_API_KEY:
            raise ValueError("Groq API key is not set.Please add it to your env file")
        if not self.TAVILY_API_KEY:
            raise ValueError("Tavily API key is not set.Please add it to your env file")
        return True


settings=Settings()