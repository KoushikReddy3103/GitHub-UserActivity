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
        response = requests.get(url, headers=HEADERS, verify=False)
        response.raise_for_status()  # Raise an error for bad responses
        if response.status_code == 200:
            events = response.json()
            return events
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the user activity: {e}")
        return None

def display_event_summary(events):
    for event in events:
        event_type = event.get('type')
        repo_name = event.get('repo', {}).get('name')
        created_at = event.get('created_at')
        print(f"Event: {event_type} | Repo: {repo_name} | Time: {created_at}")
        


