"""
Social Media Evaluation:
- Best performing engagement rate per post in which platform
- Which content it was
- Best performing engagement rate in which platform and why


Online Media Evaluation:
-Sentiments percentage
-What date is the highest for positive/neutral/negative and why
-Which media covers the most about

Reputation Analysis Evaluation:
-How many talks regarding ASDP and what sentiment
-What date is the highest for positive/neutral/negative and why
-Highest issue and regarding of what
-What kategori with the most talk and what sentiment
-Perceptions regarding
"""

import requests
import json

def request_engagement_rate(timestamp_start, timestamp_end, object_id):

    url = "https://external.backend.dashboard.nolimit.id/v1.0/social-media/engagement-rate"
    api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"


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
      "post_ownership": [],
      "validation_list": []
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            #print("Data from NoLimit API:", data)
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None


