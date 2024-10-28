import requests
import random
import os
from datetime import datetime
import openai

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DEV_TO_API_KEY = os.getenv('DEV_TO_API_KEY')

openai.api_key = OPENAI_API_KEY

# Define a function to generate a random topic using OpenAI's API
def get_random_topic():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
        messages=[
            {"role": "user", "content": "Suggest a random blog topic related to front-end technologies. It should be very less and opt to dev.to blog post"}
        ]
    )
    topic = response['choices'][0]['message']['content'].strip()
    return topic
def generate_blog_content(topic):
    
    # Use OpenAI to generate content
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": f"Write a blog post about {topic}."}
        ]
    )
    # content = response['choices'][0]['text'].strip()
    content = response['choices'][0]['message']['content'].strip()
    return content

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
    random_topic = get_random_topic()  # Get a random topic
    content = generate_blog_content(random_topic)  # Generate content for that topic
    print(f"Title: {random_topic}\nContent: {content}")
    # Publish to dev.to
    publish_to_dev_to(random_topic, content)
