import requests

def request_stream(api_key, timestamp_start, timestamp_end, object_id):

    url = "https://external.backend.dashboard.nolimit.id/v1.0/social-media/stream"
    # api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"


    headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-API-KEY": api_key
    }

    payload = {
        "timestamp_start": timestamp_start,
        "timestamp_end": timestamp_end,
        "object_ids": [object_id],
        "label_ids": [],
        "include_keywords": [],
        "exclude_keywords": [],
        "sentiment": [],
        "content_type_list": [],
        "post_ownership": ["postmade"],
        "validation_list": [],
        "page": 1,
        "size": 1,
        "column_to_sort": "comment",
        "sort_by": "desc"
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


