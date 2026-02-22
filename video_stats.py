import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='./.env')  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')  # Get API key from environment variable
CHANNEL_NAME = 'MrBeast'

def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_NAME}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        #print(response)
        #print(json.dumps(data, indent=4))
        channel_items = data['items'][0]
        channel_playlist_id = channel_items['contentDetails']['relatedPlaylists']['uploads']
        #print(channel_playlist_id)
        return channel_playlist_id
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_playlist_id()