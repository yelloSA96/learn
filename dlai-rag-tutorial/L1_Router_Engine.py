#!/usr/bin/env python
# coding: utf-8

# # Lesson 1: Router Engine

# Welcome to Lesson 1.
# 
# To access the `requirements.txt` file, the data/pdf file required for this lesson and the `helper` and `utils` modules, please go to the `File` menu and select`Open...`.
# 
# I hope you enjoy this course!

# ## Setup
from helper import get_openai_api_key
OPENAI_API_KEY = get_openai_api_key()

import nest_asyncio # 1.6.0
nest_asyncio.apply()


# ## Load Data

# To download this paper, below is the needed code:
# 
# #!wget "https://openreview.net/pdf?id=VtmBAGCN7o" -O metagpt.pdf
# 
# **Note**: The pdf file is included with this lesson. To access it, go to the `File` menu and select`Open...`.

# In[ ]:


from llama_index.core import SimpleDirectoryReader

# load documents
documents = SimpleDirectoryReader(input_files=["metagpt.pdf"]).load_data()


# ## Define LLM and Embedding model

# In[ ]:


from llama_index.core.node_parser import SentenceSplitter

splitter = SentenceSplitter(chunk_size=1024)
nodes = splitter.get_nodes_from_documents(documents)
# Nodes are just seperation of sentences of ~ 1024 chunks.

# In[ ]:


from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")


# ## Define Summary Index and Vector Index over the Same Data

# In[ ]:
# Querying a vector index, will answer with the most similar node by the embedding similary test.

from llama_index.core import SummaryIndex, VectorStoreIndex

summary_index = SummaryIndex(nodes)
vector_index = VectorStoreIndex(nodes)


# ## Define Query Engines and Set Metadata

# In[ ]:


summary_query_engine = summary_index.as_query_engine(
    response_mode="tree_summarize",
    use_async=True,
)
vector_query_engine = vector_index.as_query_engine()


# In[ ]:


from llama_index.core.tools import QueryEngineTool


summary_tool = QueryEngineTool.from_defaults(
    query_engine=summary_query_engine,
    description=(
        "Useful for summarization questions related to MetaGPT"
    ),
)

vector_tool = QueryEngineTool.from_defaults(
    query_engine=vector_query_engine,
    description=(
        "Useful for retrieving specific context from the MetaGPT paper."
    ),
)


# ## Define Router Query Engine

# In[ ]:


from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector


query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[
        summary_tool,
        vector_tool,
    ],
    verbose=True
)


# In[ ]:


response = query_engine.query("What is the summary of the document?")
print(str(response))
# Selecting query engine 0: This choice indicates that the document is useful for summarization questions related to MetaGPT, which aligns with the question asking for the summary of the document..
# The document introduces MetaGPT, a meta-programming framework that enhances multi-agent systems based on Large Language Models (LLMs) through role specialization, workflow management, and efficient communication mechanisms. It outperforms existing approaches in software development tasks, showcasing its effectiveness in code generation quality improvement. The development process of a software application named "Drawing App" is detailed, highlighting the roles of various agents like the Architect, Project Manager, Engineer, and QA Engineer. Python libraries like Tkinter and Pillow are used for GUI creation, and the testing approach involves Python's unittest library. MetaGPT's performance in generating executable code is discussed, emphasizing its structured approach in transforming abstract requirements into detailed designs. The document also addresses limitations and ethical concerns related to the system, such as information overload and privacy issues, while showcasing the overall effectiveness of MetaGPT in automating software development tasks and enhancing development process efficiency.

# In[ ]:


print(len(response.source_nodes))


# In[ ]:


# response = query_engine.query(
#     "How do agents share information with other agents?"
# )
# print(str(response))


# ## Let's put everything together

# In[ ]:


# from utils import get_router_query_engine
#
# query_engine = get_router_query_engine("metagpt.pdf")
#

# In[ ]:

#
# response = query_engine.query("Tell me about the ablation study results?")
# print(str(response))

