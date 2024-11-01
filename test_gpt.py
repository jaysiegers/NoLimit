import requests

# Replace `YOUR_API_KEY` with your actual key but don't hardcode it in production code.
api_key = "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"
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# JSON payload containing data and action details
data_payload = {
    "model": "gpt-3.5-turbo",  # Specify the model here
    "messages": [
        {
            "role": "user",
            "content": """
                Analyze the following engagement data and generate a report on the best performing social media platform:
                ID: cea93e56-3fbf-44d8-9c27-ef4a4fb831c9, Social Media: instagram, Display Name: asdp191, Stream Type: account, Value: 0.18658837635166214, Growth: 16.982%, Past: 0.15950162152016212, Content Type: engagementRate, Title: Engagement Rate
                ID: 21c2246f-333f-445b-920f-eda7433fa602, Social Media: twitter, Display Name: asdp191, Stream Type: account, Value: 0.014367816091954023, Growth: 100%, Past: 0.0065214555888874395, Content Type: engagementRate, Title: Engagement Rate
                ID: b73113bc-69a7-4245-a616-a99899fe1ff8, Social Media: twitter, Display Name: asdp, Stream Type: keyword, Value: 0, Growth: 100%, Past: 0, Content Type: engagementRate, Title: Engagement Rate
                ID: 5c237b27-8940-47f3-a4b7-e18f4da45aaa, Social Media: youtube, Display Name: asdp, Stream Type: keyword, Value: 0, Growth: 100%, Past: 0, Content Type: engagementRate, Title: Engagement Rate
                ID: 761b67f4-3886-47a3-bcec-bb9b6257e096, Social Media: instagram, Display Name: #asdp, Stream Type: keyword, Value: 0, Growth: 100%, Past: 0, Content Type: engagementRate, Title: Engagement Rate
                ID: fe65c7af-be83-431a-aa2a-119f9149bd66, Social Media: facebook, Display Name: ASDP Indonesia Ferry, Stream Type: account, Value: 0.044206016562796296, Growth: -92.459%, Past: 0.5861324376199616, Content Type: engagementRate, Title: Engagement Rate
                ID: b16a47d0-28dc-4176-9e72-d896dd9f1f83, Social Media: youtube, Display Name: ASDP Indonesia Ferry, Stream Type: account, Value: 0.36219581211092244, Growth: 73.489%, Past: 0.208771594313763, Content Type: engagementRate, Title: Engagement Rate
                ID: 815dee5a-0825-4913-8217-51de8313d69a, Social Media: tiktok, Display Name: asdp191, Stream Type: account, Value: 1.3358379800704847, Growth: 100%, Past: 0.3527180472425429, Content Type: engagementRate, Title: Engagement Rate
            """
        }
    ]
}

response = requests.post(url, headers=headers, json=data_payload)

# Check if the request was successful
if response.status_code == 200:
    report = response.json()
    print("Generated Report:")
    print(report)  # Print the returned report or process it as needed
else:
    print(f"Error: {response.status_code}")
    print(response.json())
