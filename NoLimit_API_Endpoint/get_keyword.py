import requests

def request_keyword():
    
    url = "https://external.backend.dashboard.nolimit.id/v1.0/social-media/keyword-list"
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
            return data
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None




