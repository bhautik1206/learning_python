import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv("API_Weather_KEY")
url = os.getenv("API_Weather_URL")

querystring = {"location": "", "format": "json", "u": "f"}

headers = {
    "x-rapidapi-key": API_Key,
    "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com",
    "Content-Type": "application/json"
}


def weather():
    location = input("Enter the location:")
    if location : 
        apiCall(location)    
    else:
        print("Wrong Input")

def apiCall(location):
    try:
        querystring["location"] = location
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        temp = data["current_observation"]["condition"]["temperature"]
        print(temp)
    except:
        print(response)
        print("Error is throwing")
        