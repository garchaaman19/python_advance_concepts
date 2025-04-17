## neo 4j 

# String as input but passing document objects. 

from langchain_community.document_loaders.csv_loader import CSVLoader
data = loader.load()

1. embeddings.embed_query(data) expects a string as input, but data from loader.load() returns a list of Document objects. 


# Incorrect results 
1. Added meta data, ids in vector db, irrelevant results.
2. instruction tuning

# Hallucination. 

1. RAG 
2. evaluate 


# Guard rails
- OpenAI’s moderation endpoint

    from openai import Moderation 
    moderation = Moderation.create(input=response)

- Nemo guardrails 
    

# Chroma DB 
- delete collections