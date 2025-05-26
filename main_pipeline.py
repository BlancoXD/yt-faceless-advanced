import modules.niche_discovery as niche
import modules.script_generator as scriptgen
import modules.voiceover_generator as voice
import modules.video_creator as video
import modules.thumbnail_generator as thumb
import modules.youtube_uploader as uploader
import json
import os

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = load_config()

    if config["manual_topic"]:
        topic = config["manual_topic"]
    else:
        topic = niche.discover_topic()

    print(f"Selected topic: {topic}")

    script = scriptgen.generate_script(topic)
    with open("output/scripts/last_script.txt", "w", encoding="utf-8") as f:
        f.write(script)

    audio_path = voice.text_to_speech(script, config["voice"])

    video_path = video.create_video(audio_path, topic)
    thumb.generate_thumbnail(topic)

    if config["upload_to_youtube"]:
        uploader.upload_video(
            video_path=video_path,
            title=f"{topic} - Explained",
            description=f"This video covers: {topic}.",
            tags=["AI", "automation", "faceless", "YouTube"],
            thumbnail_path="output/thumbnails/thumb_v1.png"
        )

if __name__ == "__main__":
    main()
