import requests
import json

import os
from dotenv import load_dotenv

from pathlib import Path
from dotenv import load_dotenv
import os

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).resolve().parent

# Load .env from the project folder
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found. Please check your .env file.") # Load API key from environment variable
  

CHANNEL_HANDLE = 'MrBeast'  # MrBeast's channel handle

def get_playlist_id():


    try:
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}'

        RESPONSE = requests.get(url)

        RESPONSE.raise_for_status() 

        data = RESPONSE.json()

        #print(json.dumps(data, indent=4))

        channel_items = data["items"][0]
        channel_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
            
        print(f"Channel Playlist ID: {channel_playlist_id}")
        return channel_playlist_id

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
  
    get_playlist_id()    

   