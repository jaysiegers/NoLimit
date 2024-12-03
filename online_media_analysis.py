# Percentage positive and neutral sentiment
# Peak Positive Sentiment with content
# Peak Neutral Sentiment with content
# The most reported article is by x

from NoLimit_API_Endpoint.get_total_article_by_media import request_total_article_by_media

clipping_ids = "00aa0060-4295-499c-b403-6d1bea15a020"
timestamp_start = "2024-10-01 00:00:00"
timestamp_end = "2024-10-30 23:59:00"
api_key = "6369ada0-6231-42c1-965b-6d73f2e87662"

data = request_total_article_by_media(api_key, timestamp_start, timestamp_end, clipping_ids)

if data is not None and 'result' in data:
    result = data['result']
    # print("Result:", result)
else:
    print("No article available.")
    result = [] 

total_positive = 0
total_negative = 0
total_neutral = 0
total_articles = 0

for articles in result:
    total_positive += articles['sentimentPositive']
    total_negative += articles['sentimentNegative']
    total_neutral += articles['sentimentNeutral']
    total_articles += articles['total']
    
    print(f"\nMedia: {articles['media']}")
    print(f"  - Positive Sentiment: {articles['sentimentPositive']}")
    print(f"  - Negative Sentiment: {articles['sentimentNegative']}")
    print(f"  - Neutral Sentiment: {articles['sentimentNeutral']}")
    print(f"  - Total Articles: {articles['total']}\n")

positive_percentage = (total_positive / total_articles) * 100 
negative_percentage = (total_negative / total_articles) * 100
neutral_percentage = (total_neutral / total_articles) * 100

print(" ")
print("--------------------------------------------------------------------------------------------------------------------------------")
print(" ")
print(f"Sentiment Each")
print(f"- Positive: {total_positive}")
print(f"- Negative: {total_negative}")
print(f"- Neutral: {total_neutral}\n")
print(f"Total Articles: {total_articles}\n")
print(f"Sentiment Percentages")
print(f"- Positive: {positive_percentage:.2f}%")
print(f"- Negative: {negative_percentage:.2f}%")
print(f"- Neutral: {neutral_percentage:.2f}%")