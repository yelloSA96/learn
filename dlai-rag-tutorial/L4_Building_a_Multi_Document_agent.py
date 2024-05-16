# Building a Multi-Document Agent
from helper import get_openai_api_key
OPENAI_API_KEY = get_openai_api_key()

import nest_asyncio
nest_asyncio.apply()

## Setup an agent over 3 papers
### Note: The pdf files are included with this lesson. To access these papers, go to the File menu and selectOpen....
urls = [
    "https://openreview.net/pdf?id=VtmBAGCN7o",
    "https://openreview.net/pdf?id=6PmJoRfdaK",
    "https://openreview.net/pdf?id=hSyW5go0v8",
]

papers = [
    "metagpt.pdf",
    "longlora.pdf",
    "selfrag.pdf",
]
from utils import get_doc_tools # Helper function
from pathlib import Path

paper_to_tools_dict = {}
# Download the files
for paper in papers:
    print(f"Getting tools for paper: {paper}")
    vector_tool, summary_tool = get_doc_tools(paper, Path(paper).stem)
    paper_to_tools_dict[paper] = [vector_tool, summary_tool]

# Take these files and have them as a flat list
initial_tools = [t for paper in papers for t in paper_to_tools_dict[paper]]

from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo")

len(initial_tools) # 6 because there is 1 vector tool & 1 Summary tool for each paper

from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.agent import AgentRunner

agent_worker = FunctionCallingAgentWorker.from_tools(
    initial_tools,
    llm=llm,
    verbose=True
) # Passing all 6 tools to a single agent with one llm
agent = AgentRunner(agent_worker)

# The result is that the LLM has tooling across all 3 documents as of this moment.
# It chose the right tool, vector_tool_longlora with the query and it runs both bits to give a response. Verbose mode shows the actions and then provides a final response.
response = agent.query(
    "Tell me about the evaluation dataset used in LongLoRA, "
    "and then tell me about the evaluation results"
)

# Summarisation tool across both two other files. It used summary_tool_selfrag & summary_tool_longlora. It then provided a response
response = agent.query("Give me a summary of both Self-RAG and LongLoRA")
print(str(response))

## Now across 11 documents
urls = [
    "https://openreview.net/pdf?id=VtmBAGCN7o",
    "https://openreview.net/pdf?id=6PmJoRfdaK",
    "https://openreview.net/pdf?id=LzPWWPAdY4",
    "https://openreview.net/pdf?id=VTF8yNQM66",
    "https://openreview.net/pdf?id=hSyW5go0v8",
    "https://openreview.net/pdf?id=9WD9KwssyT",
    "https://openreview.net/pdf?id=yV6fD7LYkF",
    "https://openreview.net/pdf?id=hnrB5YHoYu",
    "https://openreview.net/pdf?id=WbWtOYIzIK",
    "https://openreview.net/pdf?id=c5pwL0Soay",
    "https://openreview.net/pdf?id=TpD2aG1h0D"
]

papers = [
    "metagpt.pdf",
    "longlora.pdf",
    "loftq.pdf",
    "swebench.pdf",
    "selfrag.pdf",
    "zipformer.pdf",
    "values.pdf",
    "finetune_fair_diffusion.pdf",
    "knowledge_card.pdf",
    "metra.pdf",
    "vr_mcl.pdf"
]

# To download these papers, below is the needed code:
#
#
#     #for url, paper in zip(urls, papers):
#          #!wget "{url}" -O "{paper}"
#
#
# **Note**: The pdf files are included with this lesson. To access these papers, go to the `File` menu and select`Open...`.

from utils import get_doc_tools
from pathlib import Path

# Converting papers to tools dictorionary
paper_to_tools_dict = {}
for paper in papers:
    print(f"Getting tools for paper: {paper}")
    vector_tool, summary_tool = get_doc_tools(paper, Path(paper).stem)
    paper_to_tools_dict[paper] = [vector_tool, summary_tool]

# Indexing 1000 papers can be tricky despite context windows are increasing. Leads to issue of not being able to retrieve right information.
# Indexing the tools
all_tools = [t for paper in papers for t in paper_to_tools_dict[paper]]

# define an "object" index and retriever over these tools since these object tools are defined as py objects and not strings
from llama_index.core import VectorStoreIndex
from llama_index.core.objects import ObjectIndex

obj_index = ObjectIndex.from_objects(
    all_tools,
    index_cls=VectorStoreIndex,
)
# Object retriver for the question (This is like another vector store for toolings too)
obj_retriever = obj_index.as_retriever(similarity_top_k=3)

# QUery the indexed tooling so that it finds the right tooling for that paper
tools = obj_retriever.retrieve(
    "Tell me about the eval dataset used in MetaGPT and SWE-Bench"
)
# List of tooling that has a similartiy to the previous question based on description
tools[0].metadata
len(tools)

# Setting up the agent
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.agent import AgentRunner

agent_worker = FunctionCallingAgentWorker.from_tools(
    tool_retriever=obj_retriever, # Adds the object retriver before
    llm=llm,
    system_prompt=""" \
You are an agent designed to answer queries over a set of given papers.
Please always use the tools provided to answer a question. Do not rely on prior knowledge.\

""", # Add a system prompt to the agent if you want to guide the agent to do certain things
    verbose=True
)
agent = AgentRunner(agent_worker)

# We run query against the agent. Debug mode and then a final response with system prompt to fine tune the response
response = agent.query(
    "Tell me about the evaluation dataset used "
    "in MetaGPT and compare it against SWE-Bench"
)
print(str(response))

# Lesson learnt here, is this is not a chat so no memory and that it is using the obj.retrival to find the right tooling then to retrive the information
# it then combine the respones together
response = agent.query(
    "Compare and contrast the LoRA papers (LongLoRA, LoftQ). "
    "Analyze the approach in each paper first. "
)