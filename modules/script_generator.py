import openai
import os

def generate_script(topic):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt = f"Write a script for a 1-minute YouTube video about: {topic}. Do NOT include speaker tags, stage directions, or formatting like 'HOST:' or 'Opening shot:' — just give the narration as a clean paragraph."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("Script generation error:", e)
        return "This video explains " + topic + " in detail."
