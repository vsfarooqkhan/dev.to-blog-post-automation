import requests
import random
import os
from datetime import datetime
import openai

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DEV_TO_API_KEY = os.getenv('DEV_TO_API_KEY')

openai.api_key = OPENAI_API_KEY

# List of topics
TOPICS = ["JavaScript tips", "React best practices", "CSS tricks", "Intro to WebAssembly", "Future of AI"]

def generate_blog_content():
    # Pick a random topic
    topic = random.choice(TOPICS)
    
    # Use OpenAI to generate content
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": "Generate a blog post about AI and its impact on society."}
        ]
    )
    content = response['choices'][0]['text'].strip()
    return topic, content

def publish_to_dev_to(title, content):
    url = "https://dev.to/api/articles"
    headers = {
        "api-key": DEV_TO_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "article": {
            "title": title,
            "published": True,
            "body_markdown": content
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print("Blog posted successfully!")
    else:
        print(f"Failed to post blog. Status Code: {response.status_code}")

if __name__ == "__main__":
    # Generate blog content
    title, content = generate_blog_content()
    
    # Publish to dev.to
    publish_to_dev_to(title, content)
