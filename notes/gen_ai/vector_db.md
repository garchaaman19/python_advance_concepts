# Chroma db 


# FAISS
    - Supports Quantization. 



# Knowledge Graph 

## Neo4J 
import networkx as nx 

G = nx.Graph() 
 creating a graph 

- node2vec = Node2Vec(G, dimensions=64, walk_length=10, num_walks=100, workers=1) 

walk_length means length of each random walk that will be generated from each node.

num_walks - More walks increase computational cost but provide richer embeddings.

workers = num of parallel processing


## Node2Vec Working 
 1. Random Walks
    For each node in the graph, the algorithm generates a specified number of random walks of a given length.
2. Word2Vec
    techniques are used to learn embeddings for the nodes 


# Neo4J alternatives 
1. Azure cosmos DB Apache Gremlin

# Chroma DB 
1. Adding documents 
    ```
    collection = client.create_collection(name="example_collection")
    
    collection.add(
    documents=["This is a sample document."],
    metadatas=[{"author": "John"}],
    ids=["doc1"]
    )
    ```

2. How do you perform a similarity search in   ChromaDB?

  ```
    results = collection.query(
    query_texts=["AI technologies"],
    n_results=2
    )
    print(results["documents"])

  ```  


3. How do you handle duplicate documents or embeddings in ChromaDB?

```
collection.add(
    documents=["Duplicate document"],
    metadatas=[{"type": "duplicate"}],
    ids=["doc1"]
)

# Attempt to add a duplicate ID will raise an error
# Use update if needed:
collection.update(
    ids=["doc1"],
    documents=["Updated document"]
)

```

