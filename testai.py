import google.generativeai as genai


from main import (
    platform_post_highest_engagement_rate_data,
    post_highest_engagement_rate_data,
    highest_engagement_rate_data,
    most_comment_platform_data_list
)
genai.configure(api_key="AIzaSyByIpsd3zkJldFuApQA3mTmA_ziTXpOJyY")
model = genai.GenerativeModel("gemini-1.5-flash")

data = str(platform_post_highest_engagement_rate_data)

prompt = (
    "Summarize the following data with an engaging and structured format similar to an analytics report. "
    "Ensure that it highlights the platform, engagement rate, reasons for high engagement, top engagement days, and most liked content. "
    "Use the following structure:\n\n"
    "Pada Bulan [Month Year], PT. ASDP mencatatkan performa terbaik di [Platform] pada bagian engagement rate sebesar [percentage]% terutama karena [reason]. "
    "Selain itu, platform [Another Platform] mendapatkan total engagement tertinggi sebesar [total number] karena [reasons].\n\n"
    "PT. ASDP mendapatkan engagement tertinggi pada hari [Day] pada pukul [Time].\n\n"
    "Konten yang paling disukai di [Platform] adalah [Content Type] terutama terkait [specific details].\n\n"
    "Here is the data to be summarized:\n"
    f"{data}"
)

response = model.generate_content(prompt)

print(response.text)
