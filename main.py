from get_keyword import request_keyword
from get_engagement_rate import request_engagement_rate

# Define the URL, payload, and headers for the POST request

timestamp_start = "2024-10-01 00:00:00"
timestamp_end = "2024-10-30 23:59:00"

# Call the function
keyword_data = request_keyword()

id_list = [item['id'] for item in keyword_data['result']]

print(id_list)

engagementrate_data_list = []

for id_value in id_list:
    engagementrate_data = request_engagement_rate(timestamp_start = timestamp_start, timestamp_end = timestamp_end, object_id = id_value)
    if engagementrate_data is not None:
        engagementrate_data_list.append(engagementrate_data)


print(engagementrate_data_list)

# Use the returned data
#if keyword_data:
#    print("Processed Response Data:", keyword_data)
#else:
#    print("No data returned due to an error.")
