import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_key = os.getenv("API_NEW_KEY")
url=os.getenv("API_NEW_URL")
headers = {
        'x-api-key': API_key
}
response = requests.get(url, headers=headers)

def newsFunction():
    if response.status_code == 200:
        temp = response.json()
        
        for item in temp.get("news", []):
            if item.get("language") == "en":
                print({
                    "id": item.get("id"),
                    "title": item.get("title")
                })
    else:
        return f"Error: {response.status_code}"