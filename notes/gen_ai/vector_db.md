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