import os
import uuid
from tortoise.api import TextToSpeech

def text_to_speech(script, voice="emma"):
    try:
        tts = TextToSpeech()
        output_path = f"output/audio/{uuid.uuid4()}.wav"
        tts.tts_to_file(text=script, speaker=voice, file_path=output_path)
        print("✅ Tortoise TTS audio saved:", output_path)
        return output_path
    except Exception as e:
        print("❌ Voiceover generation failed:", e)
        return None
