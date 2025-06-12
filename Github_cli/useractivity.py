import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY') 

HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization":  api_key   
}


def get_user_activity(username):
    url =  f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the user activity: {e}")
        return None
    



