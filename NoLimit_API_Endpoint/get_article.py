import requests
import sys

from exceptions import APIError

def request_all_article(api_key, timestamp_start, timestamp_end, clipping_id):
    url = "https://external.backend.dashboard.nolimit.id/v1.0/online-media/article/get-article"

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
    "clipping_id": clipping_id,
    "limit": 100,
    "page": 1
    }


    try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()  
                return data  
            else:
                raise APIError(response.status_code, response.text)
             
    except APIError as e:
        raise e
    
    except Exception as e:
        raise RuntimeError(e)
    


