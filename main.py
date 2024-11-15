from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from gemini_model import process_social_media_analysis_response

# timestamp_start = "2024-10-01 00:00:00"
# timestamp_end = "2024-10-30 23:59:00"

app = FastAPI()

class AnalysisRequest(BaseModel):
    object_ids: List[str] = Field(..., example=["object_id_1", "object_id_2"])
    timestamp_start: str = Field(..., example="2024-10-01 00:00:00")
    timestamp_end: str = Field(..., example="2024-10-30 23:59:59")

class SocialMediaAnalysisResponse(BaseModel):
    response: str

@app.post("/social-media-analysis", response_model=SocialMediaAnalysisResponse)
def request_social_media_analysis(
    payload: AnalysisRequest, 
    x_api_key: str = Header(..., alias="X-API-KEY")
):
    """
    Endpoint to request social media analysis.
    Expects an API key in the header and object IDs in the request body.
    """
    try:
        # Use the provided data
        api_key = x_api_key  # Extract API key from headers
        object_ids = payload.object_ids
        timestamp_start = payload.timestamp_start
        timestamp_end = payload.timestamp_end

        # Pass the parameters to the social_media_analysis function
        social_media_analysis_response = process_social_media_analysis_response(
            api_key=api_key,
            object_ids=object_ids,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end
        )

        if social_media_analysis_response is None:
            raise HTTPException(status_code=500, detail="No data received from social_media_analysis()")

        return {"response": social_media_analysis_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")