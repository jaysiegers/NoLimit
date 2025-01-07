import google.generativeai as genai
from social_media_analysis import social_media_analysis
from online_media_analysis import online_media_analysis


def process_social_media_analysis_response(api_key, object_ids, timestamp_start, timestamp_end): 

    platform_post_highest_engagement_rate_data, post_highest_engagement_rate_data, highest_engagement_rate_data, highest_engagement_platform_data, highest_peaktime_data, most_comment_data, most_like_data = social_media_analysis(api_key, object_ids, timestamp_start, timestamp_end)
    genai.configure(api_key="AIzaSyD1dIAE56HNUWjnZCkE-lOAaxluXnoFOT4")
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Summarize the following data with an engaging and structured format exactly from this following structure. "
        "Ensure that it highlights the platform, engagement rate, reasons for high engagement, top engagement days, and most liked content. "
        "For long captions, please only briefly describe it so that it fits the original format"
        "Don't use/include bold (** **), escape quotes (\" \"), emojis, hashtags within the caption"
        "Use the following structure:\n\n"
        "Pada bulan [Timestamp start, Timestamp end (just take the month)], didapatkan performa terbaik di platform [platform with the highest ER] dengan engagement rate sebesar [Engagement rate value of platform with the highest ER] terutama pada konten mengenai [Caption of platform with the highest ER (max 1 sentence)]."
        "Selain itu, platform [Platform with the highest engagement] mendapatkan total engagement tertinggi sebesar [Engagement value of platform with the highest engagement]."
        "Engagement tertinggi didapat sebanyak [Value of peaktime data] pada hari [Day of peaktime data] pada pukul [Hour of peaktime data]."
        "Konten yang paling banyak dikomentari di [Platform with most commented post] adalah [Content type of most commented post] terutama terkait [Caption of most commented post (max 1 sentence)]."
        "Konten yang paling banyak disukai di [Platform with most liked post] adalah [Content type of most liked post] terutama terkait [Caption of most liked post (max 1 sentence)]."
        "Here is the data to be summarized:\n"
        f"Timestamp start = {timestamp_start}"
        f"Timestamp end = {timestamp_end}"
        f"Platform with the highest ER= {highest_engagement_rate_data['socialMedia']}"
        f"Engagement rate value of platform with the highest ER= {highest_engagement_rate_data['value']:.2f} %"
        f"Caption of platform with the highest ER= {platform_post_highest_engagement_rate_data.get('content')}"
        f"Platform with the highest engagement= {highest_engagement_platform_data['socialMedia']} "
        f"Engagement value of platform with the highest engagement= {highest_engagement_platform_data['value']} "
        f"Value of peaktime data= {highest_peaktime_data['value']}"
        f"Day of peaktime data= {highest_peaktime_data['day']}"
        f"Hour of peaktime data= {highest_peaktime_data['hour']} "
        f"Platform with most commented post= {most_comment_data['socialMedia']} "
        f"Content type of most commented post= {most_comment_data['contentType']}"
        f"Caption of most commented post= {most_comment_data['content']}"
        f"Platform with most liked post= {most_like_data['socialMedia']} "
        f"Content type of most liked post= {most_like_data['contentType']}"
        f"Caption of most liked post= {most_like_data['content']}"
        )

    genai_response = (model.generate_content(prompt)).text

    #print(genai_response)

    return genai_response


def process_online_media_analysis_response(api_key, clipping_id, timestamp_start, timestamp_end):

    positive_percentage, neutral_percentage, negative_percentage, peak_positive_date, peak_neutral_date, peak_negative_date, peak_positive_content, peak_neutral_content, peak_negative_content, most_articles_media, media_count= online_media_analysis(api_key, clipping_id, timestamp_start, timestamp_end)
    genai.configure(api_key="AIzaSyD1dIAE56HNUWjnZCkE-lOAaxluXnoFOT4")
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Summarize the following data with an engaging and structured format exactly from this following structure. "
        "For long captions, please only briefly describe it so that it fits the original format"
        "Don't use/include bold (** **), escape quotes (\" \"), emojis, hashtags within the caption"
        "Make sure that you don't skip the sentences"
        "Do not dicuss a sentiment that has a percentage of 0%"
        "Use the following structure:\n\n"
        "Pada Bulan [Timestamp start, Timestamp end (just take the month)], pemberitaan di media daring memiliki sentimen positif sebanyak [Positive sentiment percentage], sentimen netral [Neutral sentiment percentage], dan sentimen negatif sebesar [Negative sentiment percentage]. "
        "Selama periode ini, sentimen positif tertinggi terjadi pada tanggal [Date of highest positive sentiment] terkait [Caption related to positive sentiment]. "
        "Sentimen netral tertinggi terjadi pada tanggal [Date of highest neutral sentiment] terkait [Caption related to neutral sentiment]. "
        "Sentimen negatif tertinggi terjadi pada tanggal [Date of highest negative sentiment] terkait [Caption related to negative sentiment]. "
        "[Media with most articles] menjadi media yang paling banyak memberitakan dengan total [Total number of articles] pemberitaan."
        "Here is the data to be summarized:\n"
        f"Timestamp start = {timestamp_start}"
        f"Timestamp end = {timestamp_end}"
        f"Positive sentiment percentage = {positive_percentage:.2f} %"
        f"Neutral sentiment percentage = {neutral_percentage:.2f} %"
        f"Negative sentiment percentage = {negative_percentage:.2f} %"
        f"Date of highest positive sentiment = {peak_positive_date}"
        f"Caption related to positive sentiment = {peak_positive_content} "
        f"Date of highest neutral sentiment = {peak_neutral_date}"
        f"Caption related to neutral sentiment = {peak_neutral_content} "
        f"Date of highest negative sentiment = {peak_negative_date}"
        f"Caption related to negative sentiment = {peak_negative_content} "
        f"Media with most articles = {most_articles_media} "
        f"Total number of articles= {media_count[most_articles_media]} "    
        )

    genai_response = (model.generate_content(prompt)).text

    #print(genai_response)

    return genai_response
