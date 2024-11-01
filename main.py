from get_keyword import request_keyword
from get_engagement_rate import request_engagement_rate

# Define the URL, payload, and headers for the POST request
timestamp_start = "2024-10-01 00:00:00"
timestamp_end = "2024-10-30 23:59:00"

# Call the function to get keyword data
keyword_data = request_keyword()

# Extract IDs along with social media and stream type information
id_list = [
    {
        'id': item['id'],
        'socialMedia': item['socialMedia'],
        'displayName': item['displayName'],
        'streamType': item['streamType']
    }
    for item in keyword_data['result']
]

engagementrate_data_list = []

for item in id_list:
    id_value = item['id']
    engagementrate_data = request_engagement_rate(
        timestamp_start=timestamp_start,
        timestamp_end=timestamp_end,
        object_id=id_value
    )
    if engagementrate_data is not None:
        # Structure the data neatly, including social media and stream type
        formatted_data = {
            'id': id_value,
            'socialMedia': item['socialMedia'],
            'displayName': item['displayName'],
            'streamType': item['streamType'],
            'value': engagementrate_data['result']['value'],
            'growth': engagementrate_data['result']['growth'],
            'past': engagementrate_data['result']['past'],
            'contentType': engagementrate_data['result']['contentType'],
            'title': engagementrate_data['result']['title']
        }
        engagementrate_data_list.append(formatted_data)

# Print the tidied-up list with social media and stream type included
for data in engagementrate_data_list:
    print(f"ID: {data['id']}")
    print(f"  Social Media: {data['socialMedia']}")
    print(f"  Display Name: {data['displayName']}")
    print(f"  Stream Type: {data['streamType']}")
    print(f"  Value: {data['value']}")
    print(f"  Growth: {data['growth']}%")
    print(f"  Past: {data['past']}")
    print(f"  Content Type: {data['contentType']}")
    print(f"  Title: {data['title']}")
    print()