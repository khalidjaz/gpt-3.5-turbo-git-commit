import os
import sys
import requests
import json

API_KEY = os.environ.get('GPT_API_KEY')


def generate_commit_message(code):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'You are ChatGPT, a helpful AI language model. Generate a commit message for the following code:'},
            {'role': 'user', 'content': code},
        ],
        'max_tokens': 30,
        'n': 1,
        'stop': None,
        'temperature': 0.7,
    }

    # Update the URL to the correct API endpoint for GPT-4
    response = requests.post(
        'https://api.openai.com/v1/chat/completions', headers=headers, json=data)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        response_data = json.loads(response.text)
        message = response_data['choices'][0]['message']['content'].strip()
        # Use a fallback message if the generated message is empty
        if not message:
            message = "Fallback commit message"
        return message
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return "Error generating commit message"


def main():
    code = sys.argv[1]
    commit_msg = generate_commit_message(code)
    print(commit_msg)


if __name__ == '__main__':
    main()
