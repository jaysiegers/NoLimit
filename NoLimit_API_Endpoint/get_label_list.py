import requests
import json

url = "https://external.backend.dashboard.nolimit.id/v1.0/social-media/label-list"
api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-API-KEY": api_key
}

try:
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}, {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Network error occurred: {e}")


