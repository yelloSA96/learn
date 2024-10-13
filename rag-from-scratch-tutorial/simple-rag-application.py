import requests
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]

def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]


prompt = """
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""



# Reference Link - https://learnbybuilding.ai/tutorials/rag-chatbot-on-podcast-llamaindex-faiss-openai
if __name__ == '__main__':
    user_prompt = "What is a leisure activity that you like?"
    user_input = "I like to hike"
    relevant_document = return_response(user_input, corpus_of_documents)
    full_response = []

    url = 'http://localhost:11434/api/generate'
    # This parts formats the data json ready to ask the llm
    data = {
        "model": "llama2",
        "prompt": prompt.format(user_input=user_input, relevant_document=relevant_document)
    }
    print(data)

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
    try:
        count = 0
        for line in response.iter_lines():
            # filter out keep-alive new lines
            # count += 1
            # if count % 5== 0:
            #     print(decoded_line['response']) # print every fifth token
            if line:
                decoded_line = json.loads(line.decode('utf-8'))

                full_response.append(decoded_line['response'])
    finally:
        response.close()
    print(''.join(full_response))

