import requests
import json

import sys
sys.stdout.reconfigure(encoding='utf-8')

url = "https://external.backend.dashboard.nolimit.id/v1.0/online-media/article/get-article"
api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-API-KEY": api_key
}

payload = {
  "timestamp_start": "2024-10-01 00:00:00",
  "timestamp_end": "2024-10-30 23:59:00",
  # "media_list": [
  #   ""
  # ],
  "phrase": "asdp",
  "sentiment": "positive",
  "limit": 10,
  "page": 1
}

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        for item in data['result']['list']:
            print(item)

    else:
        print(f"Error: {response.status_code}, {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Network error occurred: {e}")


