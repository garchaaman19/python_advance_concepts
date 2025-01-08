## neo 4j 

# String as input but passing document objects. 

from langchain_community.document_loaders.csv_loader import CSVLoader
data = loader.load()

1. embeddings.embed_query(data) expects a string as input, but data from loader.load() returns a list of Document objects. 


# Incorrect results 
1. Added meta data, ids. 


# Hallucination. 

1. 


# Guard rails
- OpenAI’s moderation endpoint

    from openai import Moderation 
    moderation = Moderation.create(input=response)

# Chroma DB 
- delete collections