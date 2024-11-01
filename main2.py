from get_keyword import request_keyword
from get_top_post_made import request_top_post_made
from collections import Counter

# Define the URL, payload, and headers for the POST request
timestamp_start = "2024-10-01 00:00:00"
timestamp_end = "2024-10-30 23:59:00"

# Call the function to get keyword data with error handling
try:
    keyword_data = request_keyword()
    if keyword_data is None or 'result' not in keyword_data:
        print("No data received from request_keyword(). Please check the API connection.")
        keyword_data = {'result': []}  # Use an empty list as fallback to avoid further errors.
except Exception as e:
    print(f"Network error occurred while fetching keyword data: {e}")
    keyword_data = {'result': []}  # Fallback to empty data to prevent further errors.

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

top_post_made_data_list = []

# Fetch top posts made for each item in id_list
for item in id_list:
    id_value = item['id']
    try:
        top_post_made_data = request_top_post_made(
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            object_id=id_value
        )
        
        # Check if 'result' is a list and handle accordingly
        if top_post_made_data is not None:
            if isinstance(top_post_made_data['result'], list):
                # If result is a list, loop through each item in the list
                for result_item in top_post_made_data['result']:
                    formatted_data = {
                        'id': id_value,
                        'socialMedia': item['socialMedia'],
                        'displayName': item['displayName'],
                        'streamType': item['streamType'],
                        'contentType': result_item.get('contentType'),
                        'title': result_item.get('title'),
                        'link': result_item.get('link')  # Adjust this based on actual key for the post URL
                    }
                    top_post_made_data_list.append(formatted_data)
            else:
                # If result is a dictionary, process as before
                formatted_data = {
                    'id': id_value,
                    'socialMedia': item['socialMedia'],
                    'displayName': item['displayName'],
                    'streamType': item['streamType'],
                    'contentType': top_post_made_data['result'].get('contentType'),
                    'title': top_post_made_data['result'].get('title'),
                    'link': top_post_made_data['result'].get('link')  # Adjust this based on actual key for the post URL
                }
                top_post_made_data_list.append(formatted_data)
                
    except Exception as e:
        print(f"Error occurred while fetching top post data for ID {id_value}: {e}")

# Print the tidied-up list with social media and stream type included
if top_post_made_data_list:
    for data in top_post_made_data_list:
        print(f"ID: {data['id']}")
        print(f"  Social Media: {data['socialMedia']}")
        print(f"  Display Name: {data['displayName']}")
        print(f"  Stream Type: {data['streamType']}")
        print(f"  Content Type: {data['contentType']}")
        print(f"  Title: {data['title']}")
        
        # Print the link to the actual post
        if 'link' in data and data['link']:
            print(f"  Link: {data['link']}")
        
        print()
else:
    print("No top post data available.")

# Count posts per social media platform
post_counts = {}

for data in top_post_made_data_list:
    platform = data['socialMedia']
    if platform in post_counts:
        post_counts[platform] += 1
    else:
        post_counts[platform] = 1

# Print post count per social media platform
for platform, count in post_counts.items():
    print(f"Social Media: {platform}, Post Count: {count}")
