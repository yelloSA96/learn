# Deep Learning AI - CrewAI

## Overview

Overview of the elements include 
- Role Playing - LLM perform better when they are role playing. Use special key words to illustrate the way it should think. 
- Focus - use multiple agents where better results with 1 agent to 1 tool 
- Tools - providing them the key tools as if you were going to hire them. 
- Cooperation - Layouts of these agents
- Guardrails - stay on track especially open source models. 
- Memory - long term(after tasks completed), shorterm(execution of a task), entity 

Key Elements of agent tools
- Versatility - Capable of handling multiple types of inputs  
- Fault Tolerance - If the tool isn't able to get the right output, it can retry or heal from it 
- Caching - Offers cross-agent caching (If different agent's trying to get same info, able to efficiently save time & resources)

Manager Mental framework
Overview Q
- What is the goal?
- What is the process?
[People] What kind of individual would I need to hire to get the job done?
- Which processes and tasks do I expect the individual on my team to do?
  - breaking up into sub tasks
Each task considerations:
- Clear description
- set a clear and concise expectation of the outcome i.e. You've just hired a junior engineer and you need to create a clear outcome of what they're doing. 
- set context
- set a callback
- override agent tools with specific task tools
- force human input before end of task
- execute asynchronously 
- output as pydantic
- output as json
- output as file
- run in parallel

Multi-frameowkr hierarchies
- sequential
- managerial format 

## Tips
- So by default, the crew is performing sequentially 
- Use '' instead of '''''' multilined
- Think like a manager - Ask Q: What is the Goal?, Q: What is the process?, Q: What kind of people would I need to hire to get this done? -> translates into crew ai frameworks 
What are the keywords that better hone on a personality 
- Langchain tools can be used by crew ai
## Summary

## Referencial Links