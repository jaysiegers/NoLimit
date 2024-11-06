import google.generativeai as genai

from social_media_analysis import (
    platform_post_highest_engagement_rate_data,
    post_highest_engagement_rate_data,
    highest_engagement_rate_data,
    most_comment_data,
    timestamp_start,
    timestamp_end
)

def social_media_analysis(): 
    genai.configure(api_key="AIzaSyByIpsd3zkJldFuApQA3mTmA_ziTXpOJyY")
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = (
        "Summarize the following data with an engaging and structured format exactly from this following structure. "
        "Ensure that it highlights the platform, engagement rate, reasons for high engagement, top engagement days, and most liked content. "
        "For long captions, please only briefly describe it so that it fits the original format"
        "Don't use bold"
        "Use the following structure:\n\n"
        "Pada bulan [Timestamp start, Timestamp end], PT. ASDP mencatatkan performa terbaik di platform [platform] dengan engagement rate sebesar [Engagement rate value of platform with the highest ER] terutama pada konten mengenai [Caption of platform with the highest ER]. "
        #f"Selain itu, platform {post_highest_engagement_rate_data} mendapatkan total engagement rate tertinggi sebesar [total number] karena [reasons].\n\n"
        #"PT. ASDP mendapatkan engagement tertinggi pada hari [Day] pada pukul [Time].\n\n"
        "Konten yang paling banyak dikomentari di [Platform with most commented post] adalah [Content type of most commented post] terutama terkait [Caption of most commented post].\n\n"
        "Here is the data to be summarized:\n"
        f"Timestamp start = {timestamp_start}"
        f"Timestamp end = {timestamp_end}"
        f"Platform with the highest ER= {highest_engagement_rate_data['socialMedia']}"
        f"Engagement rate value of platform with the highest ER= {highest_engagement_rate_data['value']:.2f} %"
        f"Caption of platform with the highest ER= {platform_post_highest_engagement_rate_data.get('content')}"
        f"Platform with most commented post= {most_comment_data['socialMedia']} "
        f"Content type of most commented post= {most_comment_data['contentType']}"
        f"Caption of most commented post= {most_comment_data['content']}"
        )

    genai_response = (model.generate_content(prompt)).text

    # print(type(genai_response.text))
    print(genai_response)

    return genai_response