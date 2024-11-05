import google.generativeai as genai


from main import (
    platform_post_highest_engagement_rate_data,
    post_highest_engagement_rate_data,
    highest_engagement_rate_data,
    most_comment_data,
    timestamp_start,
    timestamp_end
)
genai.configure(api_key="AIzaSyByIpsd3zkJldFuApQA3mTmA_ziTXpOJyY")
model = genai.GenerativeModel("gemini-1.5-flash")

data = str(platform_post_highest_engagement_rate_data)

# prompt = (
#     "Summarize the following data with an engaging and structured format similar to an analytics report. "
#     "Ensure that it highlights the platform, engagement rate, reasons for high engagement, top engagement days, and most liked content. "
#     "Use the following structure:\n\n"
#     "Pada Bulan [Month Year], PT. ASDP mencatatkan performa terbaik di [Platform] pada bagian engagement rate sebesar [percentage]% terutama karena [reason]. "
#     "Selain itu, platform [Another Platform] mendapatkan total engagement tertinggi sebesar [total number] karena [reasons].\n\n"
#     "PT. ASDP mendapatkan engagement tertinggi pada hari [Day] pada pukul [Time].\n\n"
#     "Konten yang paling disukai di [Platform] adalah [Content Type] terutama terkait [specific details].\n\n"
#     "Here is the data to be summarized:\n"
#     f"{data}"
# )

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


from datetime import datetime

# Convert timestamp to month and year format
timestamp_start_str = datetime.strptime(timestamp_start, "%Y-%m-%d %H:%M:%S").strftime("%B %Y")
timestamp_end_str = datetime.strptime(timestamp_end, "%Y-%m-%d %H:%M:%S").strftime("%B %Y")


# Now pass this prompt to your Generative AI model


response = model.generate_content(prompt)

print(response.text)
