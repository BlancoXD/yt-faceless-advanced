import openai
import os
import json
import random

def discover_topic():
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt = "Give me 5 viral YouTube Shorts topics in any of the following categories: AI, gaming, productivity, technology, or entertainment. Avoid repeats or overly broad topics."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        topics = response.choices[0].message.content.strip().split("\n")
        cleaned = [t.strip("12345. ") for t in topics if t.strip()]
        chosen = random.choice(cleaned)

        print("✅ Discovered topic:", chosen)
        return chosen

    except Exception as e:
        print("❌ Niche discovery error:", e)
        return "Top 5 AI Tools of 2025"
