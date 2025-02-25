import os
import requests
def make_post_request(url:str, data, headers=None):
    """
    Makes a POST request to the specified URL with the given data and headers.

    :param url: The URL to which the POST request is sent.
    :param data: The data to be sent in the POST request.
    :param headers: Optional headers to include in the POST request.
    :return: Response object from the POST request.
    """
    if headers is None:
        headers = {'Content-Type': 'application/json'}

    return requests.post(url, json=data, headers=headers)


def inspect_response(response:object):
    """
    Inspects the response object and prints the content of each result.

    :param response: The response object to inspect.
    """
    try:
        json_response = response.json()
        results = json_response.get('results', [])
        for result in results:
            print(result.get('content', 'No content found'))
    except ValueError:
        print('Response is not in JSON format')


if __name__ == "__main__":
    # Example usage

    url = 'https://api.tavily.com/search'
    data = {
        'api_key': os.getenv('API_KEY'),
        'query': 'What is an aquarius good at?'
    }
    response = make_post_request(url, data)

    print(f'Status Code: {response.status_code}')
    print(f'Response Body: {response.text}')

    inspect_response(response)