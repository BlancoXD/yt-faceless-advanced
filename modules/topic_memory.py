import json
import os

MEMORY_FILE = "output/meta/topic_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_topic(topic):
    memory = load_memory()
    if topic not in memory:
        memory.append(topic)
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=2)
