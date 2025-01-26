import requests
import random
import os
from datetime import datetime
import openai

# Load API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DEV_TO_API_KEY = os.getenv('DEV_TO_API_KEY')

openai.api_key = OPENAI_API_KEY
PROMPTS = [
    "Suggest a unique and up-to-date blog topic related to front-end technologies in 2025.",
    "Provide a fresh, trending blog topic on modern front-end development practices.",
    "What are some advanced concepts in front-end development to write about today?",
    "List a current topic for a technical blog post in front-end development or React.",
    "Suggest an exciting and new blog idea for a Dev.to post on TypeScript or JavaScript frameworks."
]

# Define a function to generate a random topic using OpenAI's API
def get_random_topic():
    selected_prompt = random.choice(PROMPTS)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use "gpt-4" if you have access
        messages=[
            {"role": "user", "content": selected_prompt}
        ]
    )
    topic = response['choices'][0]['message']['content'].strip()
    return topic.strip('"')  # Remove any surrounding quotes
def generate_blog_content(topic):
    
    # Use OpenAI to generate content
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": f"Write a detailed and updated blog post about '{topic}' with recent insights."}
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
