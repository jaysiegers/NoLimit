from get_keyword import request_keyword
from get_engagement_rate import request_engagement_rate
from get_top_post_made import request_top_post_made

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

engagementrate_data_list = []

for item in id_list:
    if item['streamType'] == 'account':
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

if engagementrate_data_list:
    # Initialize with the first item in the list
    highest_engagement_rate_data = engagementrate_data_list[0]

    # Start from the second item and compare each item's engagement rate
    for data in engagementrate_data_list[1:]:
        if data['value'] > highest_engagement_rate_data['value']:
            highest_engagement_rate_data = data

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

if highest_engagement_rate_data:
    print("Account with the highest engagement rate: ")
    print(f"  Social Media: {highest_engagement_rate_data['socialMedia']}")
    print(f"  Display Name: {highest_engagement_rate_data['displayName']}")
    print(f"  Stream Type: {highest_engagement_rate_data['streamType']}")
    print(f"  Value: {highest_engagement_rate_data['value']}")
    print(f"  Growth: {highest_engagement_rate_data['growth']}%")
    print(f"  Past: {highest_engagement_rate_data['past']}")
    print(f"  Content Type: {highest_engagement_rate_data['contentType']}")
    print(f"  Title: {highest_engagement_rate_data['title']}")
    print()

top_post_made_data_list = []

# Fetch top posts made for each item in id_list
for item in id_list:
    if item['streamType'] == 'account':
        id_value = item['id']
        try:
            top_post_made_data = request_top_post_made(
                timestamp_start=timestamp_start,
                timestamp_end=timestamp_end,
                object_id=id_value
            )
            
            # Check if 'result' is a list and handle accordingly
            # if top_post_made_data is not None:
            #     if isinstance(top_post_made_data['result'], list):
                    # If result is a list, loop through each item in the list
            for result_item in top_post_made_data['result']:
                formatted_data = {
                    'id': id_value,
                    'socialMedia': result_item.get('socialMedia'),
                    'displayName': result_item.get('fromName'),
                    'streamType': item['streamType'],
                    'contentType': result_item.get('contentType'),
                    'title': result_item.get('title'),
                    'engagementRate': result_item.get('engagementRate'),
                    'shareCount': result_item.get('shareCount'),
                    'likeCount': result_item.get('likeCount'),
                    'commentCount': result_item.get('commentCount'),
                    'reach': result_item.get('reach'),
                    'impression': result_item.get('impression'),
                    'timestamp': result_item.get('timestamp'),
                    'link': result_item.get('link') # Adjust this based on actual key for the post URL
                }
                # print(formatted_data)
                top_post_made_data_list.append(formatted_data)
                # else:
                #     # If result is a dictionary, process as before
                #     formatted_data = {
                #         'id': id_value,
                #         'socialMedia': top_post_made_data['result'].get('socialMedia'),
                #         'displayName': top_post_made_data['result'].get('fromName'),
                #         'streamType': item['streamType'],
                #         'contentType': top_post_made_data['result'].get('contentType'),
                #         'title': top_post_made_data['result'].get('title'),
                #         'engagementRate': top_post_made_data.get('engagementRate'),
                #         'shareCount': top_post_made_data.get('shareCount'),
                #         'likeCount': top_post_made_data.get('likeCount'),
                #         'commentCount': top_post_made_data.get('commentCount'),
                #         'reach': top_post_made_data.get('reach'),
                #         'impression': top_post_made_data.get('impression'),
                #         'timestamp': top_post_made_data.get('timestamp'),
                #         'link': top_post_made_data['result'].get('link'),  # Adjust this based on actual key for the post URL
                #     }
                #     print('DICTIONARYYYYYYYY')
                #     print(formatted_data)
                #     top_post_made_data_list.append(formatted_data)
                    
        except Exception as e:
            print(f"Error occurred while fetching top post data for ID {id_value}: {e}")


if top_post_made_data_list:
    for data in top_post_made_data_list:
        # Initialize with the first item in the list
        post_highest_engagement_rate_data = top_post_made_data_list[0]

        # Start from the second item and compare each item's engagement rate
        for data in top_post_made_data_list[1:]:
            if data['engagementRate'] > post_highest_engagement_rate_data['engagementRate']:
                post_highest_engagement_rate_data = data


# For anisa please fix this, this is for getting the highest post engagement rate within the platform with the highest engagement rate on average
    # for data in top_post_made_data_list:
    #     if data['id'] == highest_engagement_rate_data['id']:
    #         platform_post_highest_engagement_rate_data = top_post_made_data_list[0]
    #         for data in top_post_made_data_list[1:]:
    #             if data['engagementRate'] > platform_post_highest_engagement_rate_data['engagementRate']:
    #                 platform_post_highest_engagement_rate_data = data

# if platform_post_highest_engagement_rate_data:
#     print("Highest post engagement rate in the account with the highest engagement rate: ")
#     print(f"  Social Media: {platform_post_highest_engagement_rate_data['socialMedia']}")
#     print(f"  Display Name: {platform_post_highest_engagement_rate_data['displayName']}")
#     print(f"  Stream Type: {platform_post_highest_engagement_rate_data['streamType']}")
#     print(f"  Engagement Rate: {platform_post_highest_engagement_rate_data['engagementRate']}")
#     print()



# Print the tidied-up list with social media and stream type included
if top_post_made_data_list:
    for data in top_post_made_data_list:
        print(f"ID: {data['id']}")
        print(f"  Social Media: {data['socialMedia']}")
        print(f"  Display Name: {data['displayName']}")
        print(f"  Stream Type: {data['streamType']}")
        print(f"  Content Type: {data['contentType']}")
        print(f"  Title: {data['title']}")
        print(f"  Engagement Rate: {data['engagementRate']}")
        print(f"  Share Count: {data['shareCount']}")
        print(f"  Like Count: {data['likeCount']}")
        print(f"  Comment Count: {data['commentCount']}")
        print(f"  Reach: {data['reach']}")
        print(f"  Impression: {data['impression']}")
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

if post_highest_engagement_rate_data:
    print("Post with the highest engagement rate: ")
    print(f"  Social Media: {post_highest_engagement_rate_data['socialMedia']}")
    print(f"  Display Name: {post_highest_engagement_rate_data['displayName']}")
    print(f"  Stream Type: {post_highest_engagement_rate_data['streamType']}")
    print(f"  Content Type: {post_highest_engagement_rate_data['contentType']}")
    print(f"  Title: {post_highest_engagement_rate_data['title']}")
    print(f"  Link: {post_highest_engagement_rate_data['link']}")
    print(f"  Engagement Rate: {post_highest_engagement_rate_data['engagementRate']}")
    print(f"  Share Count: {post_highest_engagement_rate_data['shareCount']}")
    print(f"  Like Count: {post_highest_engagement_rate_data['likeCount']}")
    print(f"  Comment Count: {post_highest_engagement_rate_data['commentCount']}")
    print(f"  Reach: {post_highest_engagement_rate_data['reach']}")
    print(f"  Impression: {post_highest_engagement_rate_data['impression']}")
    print(f"  Link: {post_highest_engagement_rate_data['link']}")
    print()
    print()