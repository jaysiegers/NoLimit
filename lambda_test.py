import requests


url = "https://2usz635237snqkps7wwaieeeqa0gfkho.lambda-url.ap-southeast-2.on.aws/social-media-analysis"
api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"
timestamp_start = "2024-10-01 00:00:00"
timestamp_end = "2024-10-30 23:59:00"
object_id = ["cea93e56-3fbf-44d8-9c27-ef4a4fb831c9", "21c2246f-333f-445b-920f-eda7433fa602", "fe65c7af-be83-431a-aa2a-119f9149bd66", "b16a47d0-28dc-4176-9e72-d896dd9f1f83", "815dee5a-0825-4913-8217-51de8313d69a"]


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-API-KEY": api_key
}

payload = {
    "timestamp_start": timestamp_start,
    "timestamp_end": timestamp_end,
    "object_ids": object_id,
}

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}, {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Network error occurred: {e}")

