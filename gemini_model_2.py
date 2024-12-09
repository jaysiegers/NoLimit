import google.generativeai as genai
from online_media_analysis import online_media_analysis

def process_online_media_analysis_response(api_key, clipping_id, timestamp_start, timestamp_end):

    positive_percentage, neutral_percentage, peak_positive_date, peak_neutral_date, peak_positive_content, peak_neutral_content, most_articles_media, media_count= online_media_analysis(api_key, clipping_id, timestamp_start, timestamp_end)
    genai.configure(api_key="AIzaSyByIpsd3zkJldFuApQA3mTmA_ziTXpOJyY")
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Summarize the following data with an engaging and structured format exactly from this following structure. "
        "For long captions, please only briefly describe it so that it fits the original format"
        "Don't use/include bold (** **), escape quotes (\" \"), emojis, hashtags within the caption"
        "Make sure that you don't skip the sentences"
        "Use the following structure:\n\n"
        "Pada Bulan [Timestamp start, Timestamp end], pemberitaan terkait PT. ASDP di media daring memiliki sentimen positif sebanyak [Positive sentiment percentage]%. dan sentimen netral [Neutral sentiment percentage]%. "
        "Selama periode ini, sentimen positif tertinggi terjadi pada tanggal [Date of highest positive sentiment] terkait [Caption related to positive sentiment]. "
        "Selain itu, sentimen netral tertinggi terjadi pada tanggal [Date of highest neutral sentiment] terkait [Caption related to neutral sentiment]. "
        "[Media with most articles] menjadi media yang paling banyak memberitakan PT. ASDP dengan total [Total number of articles] pemberitaan."
        "Here is the data to be summarized:\n"
        f"Timestamp start = {timestamp_start}"
        f"Timestamp end = {timestamp_end}"
        f"Positive sentiment percentage = {positive_percentage}"
        f"Neutral sentiment percentage = {neutral_percentage} %"
        f"Date of highest positive sentiment = {peak_positive_date}"
        f"Caption related to positive sentiment = {peak_positive_content} "
        f"Date of highest neutral sentiment = {peak_neutral_date}"
        f"Caption related to neutral sentiment = {peak_neutral_content} "
        f"Media with most articles = {most_articles_media} "
        f"Total number of articles= {media_count[most_articles_media]} "    
        )

    genai_response = (model.generate_content(prompt)).text

    # print(type(genai_response.text))
    print(genai_response)

    return genai_response
