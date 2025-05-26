from PIL import Image, ImageDraw, ImageFont
import os

def generate_thumbnail(topic):
    try:
        os.makedirs("output/thumbnails/", exist_ok=True)
        base = Image.new("RGB", (1280, 720), color=(0, 0, 0))

        draw = ImageDraw.Draw(base)
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if not os.path.exists(font_path):
            font_path = "arial.ttf"

        try:
            font = ImageFont.truetype(font_path, 80)
        except:
            font = ImageFont.load_default()

        draw.text((100, 300), topic.upper(), fill="white", font=font)

        path = "output/thumbnails/thumb_v1.png"
        base.save(path)
        print("✅ Thumbnail created:", path)
    except Exception as e:
        print("❌ Thumbnail generation failed:", e)
