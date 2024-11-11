from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from gemini_model import social_media_analysis

# timestamp_start = "2024-10-01 00:00:00"
# timestamp_end = "2024-10-30 23:59:00"

app = FastAPI()

class SocialMediaAnalysis(BaseModel):
    response: str

@app.post("/social-media-analysis", response_model=SocialMediaAnalysis)
def request_social_media_analysis():
    try:
        social_media_analysis_response = social_media_analysis()
        if social_media_analysis_response is None:
            raise HTTPException(status_code=500, detail="No data received from request_social_media_analysis()")
        return {"response": social_media_analysis_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")