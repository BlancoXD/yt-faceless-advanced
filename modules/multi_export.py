from moviepy.editor import VideoFileClip
import os

def export_for_shorts(original_path):
    try:
        if not os.path.exists(original_path):
            print("❌ Original video not found:", original_path)
            return None

        os.makedirs("output/shorts/", exist_ok=True)

        clip = VideoFileClip(original_path)
        clip = clip.crop(x_center=clip.w/2, width=720, height=1280)
        short_path = original_path.replace("output/videos", "output/shorts")

        clip.write_videofile(short_path, fps=30)
        print("✅ Vertical export saved:", short_path)
        return short_path

    except Exception as e:
        print("❌ Multi-platform export failed:", e)
        return None
