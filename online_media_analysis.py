from NoLimit_API_Endpoint.get_total_article_by_media import request_total_article_by_media
from NoLimit_API_Endpoint.get_article import request_all_article
from NoLimit_API_Endpoint.get_clipping import request_clipping

from exceptions import APIError

def online_media_analysis(api_key, clipping_id, timestamp_start, timestamp_end):
    positive_percentage = None
    neutral_percentage = None
    negative_percentage = None
    peak_positive_date = None
    peak_neutral_date = None
    peak_negative_date = None
    peak_positive_content = None
    peak_neutral_content = None
    peak_negative_content = None
    most_articles_media = None
    media_count = None

    if not clipping_id:
        raise APIError(status_code=400, message="Clipping ID not supplied!")
    
    try:
        clipping_data = request_clipping(api_key)
        if not clipping_data or 'result' not in clipping_data:
            raise APIError(status_code=404, message=f"Clipping not found.")
        
    except APIError as e:
        raise e
    
    except Exception as e:
        raise RuntimeError(e)
    
    if not any(clipping["id"] == clipping_id for clipping in clipping_data["result"]):
        raise APIError(status_code=400, message=f"Invalid clipping ID: {clipping_id} supplied!")
    
    try:
        data_media = request_total_article_by_media(api_key, timestamp_start, timestamp_end, clipping_id)

        if data_media is not None and 'result' in data_media:
            result_media = data_media['result']
        else:
            raise APIError(status_code=404, message="Articles not found.")
        
    except APIError as e:
        raise e
    
    except Exception as e:
        raise RuntimeError(e)


    total_positive = 0
    total_negative = 0
    total_neutral = 0
    total_articles = 0
    media_count = {}
    
    for articles in result_media:
        total_positive += articles['sentimentPositive']
        total_negative += articles['sentimentNegative']
        total_neutral += articles['sentimentNeutral']
        total_articles += articles['total']

        media = articles['media']
        media_count[media] = media_count.get(media, 0) + articles['total']

        print(f"\nMedia: {articles['media']}")
        print(f"  - Positive Sentiment: {articles['sentimentPositive']}")
        print(f"  - Negative Sentiment: {articles['sentimentNegative']}")
        print(f"  - Neutral Sentiment: {articles['sentimentNeutral']}")
        print(f"  - Total Articles: {articles['total']}\n")

    if total_articles > 0:
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
        print(f"- Neutral: {neutral_percentage:.2f}%\n")
        
        most_articles_media = max(media_count, key=media_count.get)
        print(f"Media with the most articles: {most_articles_media} ({media_count[most_articles_media]} articles)\n")
    else:
        print("No articles available for sentiment analysis.")

    data_articles = request_all_article(api_key, timestamp_start, timestamp_end, clipping_id)
    
    positive_articles = {}
    neutral_articles = {}
    negative_articles = {}

    if data_articles and "result" in data_articles and "list" in data_articles["result"]:
        articles = data_articles["result"]["list"]
        for article in articles:
            sentiment = article.get("sentiment", "N/A")
            date_published = article.get("datePublished", "N/A")
            content = article.get("content", "N/A")
            media = article.get("sourceName", "N/A")

            if sentiment == "positive":
                if date_published not in positive_articles:
                    positive_articles[date_published] = []
                positive_articles[date_published].append((content, media))

            elif sentiment == "neutral":
                if date_published not in neutral_articles:
                    neutral_articles[date_published] = []
                neutral_articles[date_published].append((content, media))

            elif sentiment == "negative":
                if date_published not in negative_articles:
                    negative_articles[date_published] = []
                negative_articles[date_published].append((content, media))

    if positive_articles:
        peak_positive_date = max(positive_articles, key=lambda x: len(positive_articles[x]))
        peak_positive_content = positive_articles[peak_positive_date]
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print(f"\nPeak Positive Sentiment Date: {peak_positive_date}")
        print(" ")
        for content, media in peak_positive_content:
            print(f"Media: {media}\n")
            print(f"- {content}")
    else:
        print("No positive sentiment articles found.")

    print(" ")

    if neutral_articles:
        peak_neutral_date = max(neutral_articles, key=lambda x: len(neutral_articles[x]))
        peak_neutral_content = neutral_articles[peak_neutral_date]
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print(f"\nPeak Neutral Sentiment Date: {peak_neutral_date}")
        print(" ")
        for content, media in peak_neutral_content:
            print(f"Media: {media}\n")
            print(f"- {content}")
    else:
        print("No neutral sentiment articles found.")

    if negative_articles:
        peak_negative_date = max(negative_articles, key=lambda x: len(negative_articles[x]))
        peak_negative_content = negative_articles[peak_negative_date]
    else:
        print("No negative sentiment articles found.")


    return positive_percentage, neutral_percentage, negative_percentage, peak_positive_date, peak_neutral_date, peak_negative_date, peak_positive_content, peak_neutral_content, peak_negative_content, most_articles_media, media_count
