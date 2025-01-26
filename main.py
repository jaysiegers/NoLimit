from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
from mangum import Mangum
from typing import List, Dict, Any
from gemini_model import generate_social_media_analysis_summary, generate_online_media_analysis_summary
from exceptions import APIError


app = FastAPI()
handler = Mangum(app)

class SocialMediaAnalysisRequest(BaseModel):
    object_ids: List[str] = Field(..., example=["object_id_1", "object_id_2"])
    timestamp_start: str = Field(..., example="2024-10-01 00:00:00")
    timestamp_end: str = Field(..., example="2024-10-30 23:59:59")

class SocialMediaAnalysisResponse(BaseModel):
    response: str

class OnlineMediaAnalysisRequest(BaseModel):
    clipping_id: str = Field(..., example="clipping_id_1")
    timestamp_start: str = Field(..., example="2024-10-01 00:00:00")
    timestamp_end: str = Field(..., example="2024-10-30 23:59:59")

class OnlineMediaAnalysisResponse(BaseModel):
    response: str

@app.post("/social-media-analysis-summary", response_model=SocialMediaAnalysisResponse)
def request_social_media_analysis_summary(
    payload: SocialMediaAnalysisRequest, 
    x_api_key: str = Header(..., alias="X-API-KEY")
):
    """
    Endpoint to request social media analysis.
    Expects an API key in the header and object IDs in the request body.
    """
    try:
        api_key = x_api_key
        object_ids = payload.object_ids
        timestamp_start = payload.timestamp_start
        timestamp_end = payload.timestamp_end

        social_media_analysis_summary = generate_social_media_analysis_summary(
            api_key=api_key,
            object_ids=object_ids,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end
        )

        if social_media_analysis_summary is None:
            raise HTTPException(status_code=500, detail="No data received from social_media_analysis()")

        return {"response": social_media_analysis_summary}
    
    except APIError as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error occurred: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@app.post("/online-media-analysis-summary", response_model=OnlineMediaAnalysisResponse)
def request_online_media_analysis_summary(
    payload: OnlineMediaAnalysisRequest, 
    x_api_key: str = Header(..., alias="X-API-KEY")
):
    """
    Endpoint to request online media analysis.
    Expects an API key in the header and clipping IDs in the request body.
    """
    try:
        api_key = x_api_key
        clipping_id = payload.clipping_id
        timestamp_start = payload.timestamp_start
        timestamp_end = payload.timestamp_end

        online_media_analysis_summary = generate_online_media_analysis_summary(
            api_key=api_key,
            clipping_id=clipping_id,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end
        )

        if online_media_analysis_summary is None:
            raise HTTPException(status_code=500, detail="No data received from online_media_analysis()")

        return {"response": online_media_analysis_summary}
    
    except APIError as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error occurred: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")