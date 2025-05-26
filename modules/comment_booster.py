import random

def generate_pinned_comment(topic):
    templates = [
        f"What do you think about {topic.lower()}?",
        f"Have you used any tools mentioned in this video?",
        f"Let me know your thoughts on {topic.lower()} below 👇",
        f"Which one was your favorite from this list?",
        f"Did I miss anything important about {topic.lower()}?"
    ]
    return random.choice(templates)
