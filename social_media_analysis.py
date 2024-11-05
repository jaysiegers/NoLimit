from get_keyword import request_keyword
from get_engagement_rate import request_engagement_rate
from get_top_post_made import request_top_post_made
from get_stream import request_stream

import sys
sys.stdout.reconfigure(encoding='utf-8')

timestamp_start = "2024-10-01 00:00:00"
timestamp_end = "2024-10-30 23:59:00"

try:
    keyword_data = request_keyword()
    if keyword_data is None or 'result' not in keyword_data:
        print("No data received from request_keyword(). Please check the API connection.")
        keyword_data = {'result': []}
except Exception as e:
    print(f"Network error occurred while fetching keyword data: {e}")
    keyword_data = {'result': []} 


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
    highest_engagement_rate_data = engagementrate_data_list[0]
    for data in engagementrate_data_list[1:]:
        if data['value'] > highest_engagement_rate_data['value']:
            highest_engagement_rate_data = data

print(" ")
print("Engagement Rate Data List:")
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
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Account with the highest engagement rate: ")
    print(f"  ID: {highest_engagement_rate_data['id']}")
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

for item in id_list:
    if item['streamType'] == 'account':
        id_value = item['id']
        try:
            top_post_made_data = request_top_post_made(
                timestamp_start=timestamp_start,
                timestamp_end=timestamp_end,
                object_id=id_value
            )

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
                    'link': result_item.get('link')
                }
                top_post_made_data_list.append(formatted_data)
                    
        except Exception as e:
            print(f"Error occurred while fetching top post data for ID {id_value}: {e}")


if top_post_made_data_list:
    for data in top_post_made_data_list:
        post_highest_engagement_rate_data = top_post_made_data_list[0]
        for data in top_post_made_data_list[1:]:
            if data.get('engagementRate') > post_highest_engagement_rate_data.get('engagementRate'):
                post_highest_engagement_rate_data = data

    if highest_engagement_rate_data:
        platform_post_highest_engagement_rate_list = request_top_post_made(timestamp_start=timestamp_start,
                                                                        timestamp_end=timestamp_end,
                                                                        object_id=highest_engagement_rate_data['id'])
        
        for data in platform_post_highest_engagement_rate_list['result']:
            platform_post_highest_engagement_rate_data = platform_post_highest_engagement_rate_list['result'][0]
            for data in platform_post_highest_engagement_rate_list['result'][1:]:
                if data['engagementRate'] > platform_post_highest_engagement_rate_data['engagementRate']:
                    platform_post_highest_engagement_rate_data = data

most_comment_platform_data_list = []

for item in id_list:
    if item['streamType'] == 'account':
        id_value = item['id']
        try:
            most_comment_platform_data = request_stream(
                timestamp_start=timestamp_start,
                timestamp_end=timestamp_end,
                object_id=id_value
            )
            if most_comment_platform_data:
                formatted_data = {
                    'timestamp': most_comment_platform_data['result']['list'][0]['timestamp'],
                    'socialMedia': most_comment_platform_data['result']['list'][0]['socialMedia'],
                    'fromName': most_comment_platform_data['result']['list'][0]['fromName'],
                    'keywordStreamType': most_comment_platform_data['result']['list'][0]['keyword']['streamType'],
                    'link': most_comment_platform_data['result']['list'][0]['link'],
                    'engagementRate': most_comment_platform_data['result']['list'][0]['engagementRate'],
                    'commentCount': most_comment_platform_data['result']['list'][0]['commentCount'],
                    'engagement': most_comment_platform_data['result']['list'][0]['engagement'],
                    'content': most_comment_platform_data['result']['list'][0]['content'],
                    'contentType': most_comment_platform_data['result']['list'][0]['contentType'],
                    'id': most_comment_platform_data['result']['list'][0]['id']
                }
                most_comment_platform_data_list.append(formatted_data)

        except Exception as e:
            print(f"Error occurred while fetching top post data for ID {id_value}: {e}")

if len(most_comment_platform_data_list) > 1:
    most_comment_data = most_comment_platform_data_list[0]
    for data in most_comment_platform_data_list[1:]:
        if data['commentCount'] > most_comment_data['commentCount']:
            most_comment_data = data
            print(most_comment_data)
    else:
        most_comment_data = most_comment_platform_data_list[0] 
        print(most_comment_data)


if platform_post_highest_engagement_rate_list:
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Highest post engagement rate in the account with the highest engagement rate: ")
    print(f"  Social Media: {platform_post_highest_engagement_rate_data.get('socialMedia')}")
    print(f"  Display Name: {platform_post_highest_engagement_rate_data.get('fromName')}")
    print(f"  Stream Type: {platform_post_highest_engagement_rate_data.get('streamType')}")
    print(f"  Caption: {platform_post_highest_engagement_rate_data.get('content')}")
    print(f"  Engagement Rate: {platform_post_highest_engagement_rate_data.get('engagementRate')}")
    print()

if top_post_made_data_list:
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Top post made data list: ")
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
    
print("--------------------------------------------------------------------------------------------------------------------------------")
print(" ")

post_counts = {}

for data in top_post_made_data_list:
    platform = data['socialMedia']
    if platform in post_counts:
        post_counts[platform] += 1
    else:
        post_counts[platform] = 1

for platform, count in post_counts.items():
    print(f"Social Media: {platform}, Post Count: {count}")
    
print()

if post_highest_engagement_rate_data:
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Post with the highest engagement rate: ")
    print(f"  Social Media: {post_highest_engagement_rate_data['socialMedia']}")
    print(f"  Display Name: {post_highest_engagement_rate_data['displayName']}")
    print(f"  Stream Type: {post_highest_engagement_rate_data['streamType']}")
    print(f"  Content Type: {post_highest_engagement_rate_data['contentType']}")
    print(f"  Title: {post_highest_engagement_rate_data['title']}")
    print(f"  Engagement Rate: {post_highest_engagement_rate_data['engagementRate']}")
    print(f"  Share Count: {post_highest_engagement_rate_data['shareCount']}")
    print(f"  Like Count: {post_highest_engagement_rate_data['likeCount']}")
    print(f"  Comment Count: {post_highest_engagement_rate_data['commentCount']}")
    print(f"  Reach: {post_highest_engagement_rate_data['reach']}")
    print(f"  Impression: {post_highest_engagement_rate_data['impression']}")
    print(f"  Link: {post_highest_engagement_rate_data['link']}")
    print()    

if(most_comment_platform_data_list):
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Post with the highest comment on each platform: ")
    for data in most_comment_platform_data_list:
        print(f"  Time Stamp: {data['timestamp']}")
        print(f"  Social Media: {data['socialMedia']}")
        print(f"  From Name: {data['fromName']}")
        print(f"  Keyword Stream Type: {data['keywordStreamType']}")
        print(f"  Link: {data['link']}")
        print(f"  Engagement Rate: {data['engagementRate']}")
        print(f"  Engagement: {data['engagement']}")
        print(f"  Comment Count: {data['commentCount']}")
        print(f"  Content: {data['content']}")
        print(f"  Content Type: {data['contentType']}")
        print(f"  ID: {data['id']}")
        print()

if(most_comment_data):
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Post with the highest comment: ")
    print(f"  Time Stamp: {most_comment_data['timestamp']}")
    print(f"  Social Media: {most_comment_data['socialMedia']}")
    print(f"  From Name: {most_comment_data['fromName']}")
    print(f"  Keyword Stream Type: {most_comment_data['keywordStreamType']}")
    print(f"  Link: {most_comment_data['link']}")
    print(f"  Engagement Rate: {most_comment_data['engagementRate']}")
    print(f"  Engagement: {most_comment_data['engagement']}")
    print(f"  Comment Count: {most_comment_data['commentCount']}")
    print(f"  Content: {most_comment_data['content']}")
    print(f"  Content Type: {most_comment_data['contentType']}")
    print(f"  ID: {most_comment_data['id']}")
    print()