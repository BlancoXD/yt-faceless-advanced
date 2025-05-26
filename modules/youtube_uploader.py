import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(video_path, title, description, tags, thumbnail_path):
    try:
        scopes = ["https://www.googleapis.com/auth/youtube.upload"]
        creds = None

        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes)
            creds = flow.run_local_server(port=0)
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)

        youtube = build("youtube", "v3", credentials=creds)

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "tags": tags
                },
                "status": {
                    "privacyStatus": "public"
                }
            },
            media_body=MediaFileUpload(video_path)
        )
        response = request.execute()
        print("✅ Uploaded to YouTube:", response.get("id"))

        if thumbnail_path and os.path.exists(thumbnail_path):
            youtube.thumbnails().set(
                videoId=response["id"],
                media_body=MediaFileUpload(thumbnail_path)
            ).execute()
            print("✅ Thumbnail uploaded.")

    except Exception as e:
        print("❌ YouTube upload failed:", e)
