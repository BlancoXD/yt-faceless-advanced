def get_voice_persona(name):
    presets = {
        "emma": {
            "tone": "calm",
            "style": "educational",
        },
        "kya": {
            "tone": "energetic",
            "style": "fun + fast-paced",
        },
        "nova": {
            "tone": "mysterious",
            "style": "documentary",
        }
    }
    return presets.get(name.lower(), presets["emma"])
