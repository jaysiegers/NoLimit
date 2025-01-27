import requests
from exceptions import APIError

def request_clipping(api_key):
    
    url = "https://external.backend.dashboard.nolimit.id/v1.0/online-media/clipping-list"

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
            raise APIError(response.status_code, response.text)
        
    except APIError as e:
        raise e
    
    except Exception as e:
        raise RuntimeError(e)

