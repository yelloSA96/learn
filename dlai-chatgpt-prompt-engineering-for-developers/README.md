# 

## L2
Principle 1: Write clear and specific instrucitons
clear does not mean short!

Tactic 1: Use delimiters to clearly indiciate distinct parts of the input.
Delimiters can be anything like: ```, """, <>, <tag></tag>
This makes it hard for llm prompt injections! 

Tactic 2: Ask for a structured outputt
I.E. JSON, HTML

Tactic 3: Check whether conditions are satisfied.
Check assumptions required to do the task. Considerations for edge cases too for unexpected results or errors. 

Tactic 4: Few-shot prompting
Give successful examples of completing tasks. Then ask model to perform the task. 

Principle 2: Give the model time to "think"
Make a chain of reasoning before it provides its answer. It may make an assumptions and lead to the wrong answer. 
Tactic 1: Specify the steps required to complete a task
(This approach example has a good transition to idea of langchaining)

Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion.

Model Limitations: Hallucinations (Make statements that sound plausible but are not true)
Possible solution is to First find relevant information, then answer the question based on the relevant information.

## L3
- Unlikey to get at production prompt at the beginning. 
ML Iterative prompt Development
... -> Idea -> Implementation(code/data) -> Experimental results -> Error Analysis -> Repeat...
Prompting
... -> Idea -> Implementation(code/data) prompt -> Experimental results -> Error Analysis -> Repeat...

Prompt guidelines:
- Be clear and specific
- Analyse why result does not give desired output (What is the issue with the response?)
- Refine the idea and the prompt
- Repeat

![Iterative Prompt Development](./images/iterative-prompt-development.png)

Having good processes to developemtn is best way to develop prompts.
For early application, having a single prompt developed over time, for mature application, a framework that could batch test against different examples.

## L3 - Summarising
Summarising with different focuses.

## L4 - Inferring


