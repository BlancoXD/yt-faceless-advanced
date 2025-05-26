from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip
import os
import uuid
import random

def create_video(audio_path, topic):
    try:
        # Pick a background image (placeholder logic)
        image_path = f"assets/bg_default.jpg"
        if not os.path.exists(image_path):
            print("❌ Missing background image:", image_path)
            return None

        audio = AudioFileClip(audio_path)
        image = ImageClip(image_path).set_duration(audio.duration)

        video = CompositeVideoClip([image.set_audio(audio)])
        output_path = f"output/videos/{uuid.uuid4()}.mp4"
        video.write_videofile(output_path, fps=24)

        print("✅ Video saved:", output_path)
        return output_path
    except Exception as e:
        print("❌ Video generation failed:", e)
        return None
