# Lesson 3: Building an Agent Reasoning Loop
## Setup
from helper import get_openai_api_key
OPENAI_API_KEY = get_openai_api_key()

import nest_asyncio
nest_asyncio.apply()

## Load the data
# To download this paper, below is the needed code:
#!wget "https://openreview.net/pdf?id=VtmBAGCN7o" -O metagpt.pdf
# **Note**: The pdf file is included with this lesson. To access it, go to the `File` menu and select`Open...`.

### Setup the query Tools

from utils import get_doc_tools # This is similar to previous lessons utilities but from a package
vector_tool, summary_tool = get_doc_tools("metagpt.pdf", "metagpt")

### Setup Function Calling Agent
# Reference Link - https://docs.llamaindex.ai/en/stable/examples/agent/agent_runner/agent_runner/
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo", temperature=0)

from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.agent import AgentRunner

# This is the reasoning/planning module where the agent runner & angent worker are interacting with each other
agent_worker = FunctionCallingAgentWorker.from_tools(
    [vector_tool, summary_tool],
    llm=llm,
    verbose=True
)
# Think of the agent runner as the manager to the agent worker
agent = AgentRunner(agent_worker)
response = agent.query(
    "Tell me about the agent roles in MetaGPT, "
    "and then how they communicate with each other."
)
# Verbose: Calling the summary tool with input and output answering the first part of the question. It's performance varys between which llm.
# Verbose: Re-runs the query with summary tool to then answer the second part
# Then the llm responds with a final response

# This allows us to inspect the contents of the meta information
print(response.source_nodes[0].get_content(metadata_mode="all"))

# So far the conversation has been stateless without any memory. The following agent.chat allows the agent to remember previous interactions
response = agent.chat(
    "Tell me about the evaluation datasets used."
)
# To answer this, it needs to be check history
# In doing this, it reads the history
response = agent.chat("Tell me the results over one of the above datasets.")

### Lower-level: Debuggability and Control
agent_worker = FunctionCallingAgentWorker.from_tools(
    [vector_tool, summary_tool],
    llm=llm,
    verbose=True
)
agent = AgentRunner(agent_worker)
# Different from above
task = agent.create_task(
    "Tell me about the agent roles in MetaGPT, "
    "and then how they communicate with each other."
)
# Calls the summary tool and stops there and so iteratively stepping through instead of just letting the agent conduct it's activities on it's own
step_output = agent.run_step(task.task_id)

# Can debug the steps
completed_steps = agent.get_completed_steps(task.task_id)
print(f"Num completed for task {task.task_id}: {len(completed_steps)}")
print(completed_steps[0].output.sources[0].raw_output)

# inspect the next steps from current step
upcoming_steps = agent.get_upcoming_steps(task.task_id)
print(f"Num upcoming steps for task {task.task_id}: {len(upcoming_steps)}")
upcoming_steps[0]

# Added user question to memory as an async
step_output = agent.run_step(
    task.task_id, input="What about how agents share information?"
)
# Runs through the tasks ids
step_output = agent.run_step(task.task_id)
print(step_output.is_last) # Boolean
response = agent.finalize_response(task.task_id)
# Prints the last final response
print(str(response))