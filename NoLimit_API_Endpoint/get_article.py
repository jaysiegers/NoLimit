import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')


def request_all_article(api_key, timestamp_start, timestamp_end, clipping_ids):
    url = "https://external.backend.dashboard.nolimit.id/v1.0/online-media/article/get-article"
    api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"


    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-API-KEY": api_key
    }

    payload = {
    "timestamp_start": timestamp_start,
    "timestamp_end": timestamp_end,
    "media_list": [],
    "include_phrases": [],
    "sentiment": ["positive", "negative", "neutral"],
    "clipping_id": clipping_ids,
    "limit": 100,
    "page": 1
    }


    try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()  
                return data  
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return None  
    except requests.exceptions.RequestException as e:
            print(f"Network error occurred: {e}")
            return None
    


