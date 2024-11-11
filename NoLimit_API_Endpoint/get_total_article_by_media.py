import requests
import json

url = "https://external.backend.dashboard.nolimit.id/v1.0/online-media/article/total-article-by-media"
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
    #     ""
    # ],
    "phrase": "asdp",
    "sentiment": "positive"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        id_list = [
    {
        'name': item['name'],
    }
    for item in data['result']
        ]
        print(data)
        for item in id_list:
            print(item)
    else:
        print(f"Error: {response.status_code}, {response.text}")
        
except requests.exceptions.RequestException as e:
    print(f"Network error occurred: {e}")


