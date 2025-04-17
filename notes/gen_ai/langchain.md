# ReACT 
 1. How it works 
 - Understands the query, functions as reasoning agent to see which tool to select.
 - Next it parsers the output to either final answer or lists down the action and thought it had taken, Whatever is defined in the prompt. 
 - final is the observation i.e the result of the action

    - If all doesn't seem ok, It goes back to the agent and repeats the process. 


# Components of Langchain 
1. PromptTemplate 



2. Agent 
    1. React Agent   
    - agent=create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)
    2. Agent executor 
    - agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True,handle_parsing_errors=True)
    result=agent_executor.invoke(input={"input":prompt_template.format_prompt(name_of_the_person=name)})
  
3. Tools  
    - we specify description in tools.
    - tools have access to different functions. 

4. Chunking 
    - text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
  separators=[
        "\n\n",
        "\n",
        " ",
        ".",
        ",",
        "\u200b",  # Zero-width space
        "\uff0c",  # Fullwidth comma
        "\u3001",  # Ideographic comma
        "\uff0e",  # Fullwidth full stop
        "\u3002",  # Ideographic full stop
        "",
    ],
)


5. Hybrid search using Retriever
    - BM25 - works on rank - ranks top 25, most frequent words
    - bm25_retriever = BM25Retriever.from_documents(chunks)
    - hybrid_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.5, 0.5]  # Equal weight to both
)

6. Chains used 
    - RetrievalQA