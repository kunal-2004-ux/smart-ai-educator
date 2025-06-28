import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Get Together.ai API key from environment variables
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
API_URL = "https://api.together.xyz/v1/chat/completions"

def get_story_explanation(topic):
    try:
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a storytelling tutor who explains concepts through engaging stories."
                },
                {
                    "role": "user",
                    "content": f"Tell a creative, engaging story that teaches the concept of {topic}."
                }
            ],
            "max_tokens": 300,
            "temperature": 0.7
        }
        
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        story = response.json()["choices"][0]["message"]["content"]
        return story

    except Exception as e:
        print(f"[ERROR] Story generation failed: {e}")
        return f"Error generating story explanation: {e}"
