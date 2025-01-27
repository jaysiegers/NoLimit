from NoLimit_API_Endpoint.get_keyword import request_keyword
from NoLimit_API_Endpoint.get_engagement_rate import request_engagement_rate
from NoLimit_API_Endpoint.get_top_post_made import request_top_post_made
from NoLimit_API_Endpoint.get_engagement import request_engagement
from NoLimit_API_Endpoint.get_peaktime import request_peaktime
from NoLimit_API_Endpoint.get_stream import request_stream

from exceptions import APIError

def social_media_analysis(api_key, object_ids, timestamp_start, timestamp_end):
    platform_post_highest_engagement_rate_data = None
    highest_engagement_rate_data = None
    highest_engagement_platform_data = None
    highest_peaktime_data = None
    most_comment_data = None
    most_like_data = None

    if len(object_ids) == 0:
        raise APIError(status_code=400, message="Object ID not supplied!")
    
    # if object_ids == False:
    #     raise APIError(status_code=400, message="Object ID not supplied!")

    try:
        keyword_data = request_keyword(api_key)
        if not keyword_data or 'result' not in keyword_data:
            raise APIError(status_code=404, message=f"Keyword/account not found.")
        
    except APIError as e:
        raise e
    
    except Exception as e:
        raise RuntimeError(e)
    
    # Check if each object_id is in keyword_data['result']
    invalid_object_ids = []
    for object_id in object_ids:
        if not any(item['id'] == object_id for item in keyword_data['result']):
            invalid_object_ids.append(object_id)

    if invalid_object_ids:
        invalid_ids_message = ', '.join(str(id) for id in invalid_object_ids)
        raise APIError(status_code=400, message=f"Invalid object ID: {invalid_ids_message} supplied!")

    
    object_id_set = {item for item in object_ids}
    id_list = [
        {
        'id': item['id'],
        'socialMedia': item['socialMedia'],
        'displayName': item['displayName'],
        'streamType': item['streamType']
        }
        for item in keyword_data['result']
        if item['id'] in object_id_set
    ]


    # Platform with the highest engagement rate

    for item in id_list:
        if item['streamType'] == 'account':
            id_value=item['id']
            try:
                engagementrate_data = request_engagement_rate(
                    api_key=api_key,
                    timestamp_start=timestamp_start,
                    timestamp_end=timestamp_end,
                    object_id=id_value
                )
                if engagementrate_data:
                    formatted_data = {
                        'id': item['id'],
                        'socialMedia': item['socialMedia'],
                        'displayName': item['displayName'],
                        'streamType': item['streamType'],
                        'value': engagementrate_data['result']['value'],
                        'growth': engagementrate_data['result']['growth'],
                        'past': engagementrate_data['result']['past'],
                        'contentType': engagementrate_data['result']['contentType'],
                        'title': engagementrate_data['result']['title']
                    }

                    if (
                        highest_engagement_rate_data is None
                        or formatted_data['value'] > highest_engagement_rate_data['value']
                    ):
                        highest_engagement_rate_data = formatted_data

            except APIError as e:
                raise e

            except Exception as e:
                raise RuntimeError(f"Error occurred while fetching engagement rate data for ID {id_value}: {e}")



    # Top post within the patform with the highest engagement rate

    if highest_engagement_rate_data:
        id_value = highest_engagement_rate_data['id']
        try:
            top_posts = request_top_post_made(
                api_key=api_key,
                timestamp_start=timestamp_start,
                timestamp_end=timestamp_end,
                object_id=id_value
            )
            if top_posts and 'result' in top_posts and top_posts['result']:
                platform_post_highest_engagement_rate_data = max(
                    top_posts['result'],
                    key=lambda post_data: post_data.get('engagementRate', 0)
                )
            else:
                raise
        except Exception as e:
                 raise RuntimeError(f"Error occurred while fetching top posts data for ID: {e}")
    # else:
    #     print("No highest engagement rate data found to process top posts.")



# Platform with the highest engagement
    engagement_platform_data_list = []

    for item in id_list:
        if item['streamType'] == 'account':
            id_value = item['id']
            try:
                engagement_platform_data = request_engagement(
                    api_key=api_key,
                    timestamp_start=timestamp_start,
                    timestamp_end=timestamp_end,
                    object_id=id_value
                )
                if engagement_platform_data:
                    engagement_platform_data_list.append({
                        'value': engagement_platform_data['result']['value'],
                        'socialMedia': item['socialMedia']
                    })

                    highest_engagement_platform_data = max(engagement_platform_data_list, key=lambda x: x['value'], default=None)

            except Exception as e:
                print(f"Error occurred while fetching engagement data for ID {id_value}: {e}")



    object_id_list_all = []

    for item in id_list:
        object_id_list_all.append(item['id'])

    # Peaktime (the time with the highest engagement)
    try:
        peaktime_data = request_peaktime(
            api_key=api_key,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end,
            object_id=object_id_list_all
        )
        highest_peaktime_data = max(peaktime_data['result']['values'], key=lambda x: x['value'])

    except Exception as e:
        print(f"Error occurred while fetching peak time data: {e}")

    
    # Single post with the most comments and the most likes
    stream_data_list = []

    for item in id_list:
        if item['streamType'] == 'account':
            id_value = item['id']
            try:
                stream_data = request_stream(
                    api_key=api_key,
                    timestamp_start=timestamp_start,
                    timestamp_end=timestamp_end,
                    object_id=id_value
                    )
                
                if stream_data:
                    stream_data_list.append({
                        'socialMedia': stream_data['result']['list'][0]['socialMedia'],
                        'commentCount': stream_data['result']['list'][0]['commentCount'],
                        'likeCount': stream_data['result']['list'][0]['likeCount'],
                        'content': stream_data['result']['list'][0]['content'],
                        'contentType': stream_data['result']['list'][0]['contentType'],
                    })

                if stream_data:
                    most_comment_data = max(
                        stream_data_list,
                        key=lambda stream_data: stream_data['commentCount']
                        )
                else:
                    most_comment_data = None

                if stream_data:
                    most_like_data = max(
                        stream_data_list,
                        key=lambda stream_data: stream_data['likeCount']
                    )
                else:
                    most_like_data = None

            except Exception as e:
                print(f"Error occurred while fetching stream data for ID {id_value}: {e}")


    return (
    highest_engagement_rate_data,
    platform_post_highest_engagement_rate_data,
    highest_engagement_platform_data,
    highest_peaktime_data,
    most_comment_data,
    most_like_data
    )

# api_key = "6369ada0-6231-42c1-965b-6d73f2e8662"
# timestamp_start = "2024-10-01 00:00:00"
# timestamp_end = "2024-10-30 23:59:00"
# object_id = ["cea93e56-3fbf-44d8-9c27-ef4a4fb831c9", "21c2246f-333f-445b-920f-eda7433fa602", "fe65c7af-be83-431a-aa2a-119f9149bd66", "b16a47d0-28dc-4176-9e72-d896dd9f1f83", "815dee5a-0825-4913-8217-51de8313d69a"]
# social_media_analysis(api_key=api_key, timestamp_start=timestamp_start, timestamp_end=timestamp_end, object_ids=object_id)

