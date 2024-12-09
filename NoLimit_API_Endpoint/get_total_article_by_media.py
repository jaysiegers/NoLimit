import requests

def request_total_article_by_media(api_key, timestamp_start, timestamp_end, clipping_id):
    url = "https://external.backend.dashboard.nolimit.id/v1.0/online-media/article/total-article-by-media"

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
        "sentiment": [],  
        "clipping_id": clipping_id
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
    
