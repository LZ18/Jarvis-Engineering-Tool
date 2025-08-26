import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env and get API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API key not found.")
    exit()

# Create OpenAI client (new in v1.x)
client = OpenAI(api_key=api_key)

# Send a prompt to ChatGPT (gpt-4)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    max_tokens=100,
    temperature=0.7,    # Adjust for creativity (0.0 = deterministic, 1.0 = very creative)
    messages=[
        {"role": "system", "content": "You are Jarvis, a helpful assistant."},
        {"role": "user", "content": "Hello Jarvis, what can you do?"}
    ]
)

print("✅ API key loaded. Jarvis says:")
print(response.choices[0].message.content)
