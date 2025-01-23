from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
from mangum import Mangum
from typing import List, Dict, Any
from gemini_model import process_social_media_analysis_response, process_online_media_analysis_response
from exceptions import APIError


app = FastAPI()
handler = Mangum(app)

class AnalysisRequest(BaseModel):
    object_ids: List[str] = Field(..., example=["object_id_1", "object_id_2"])
    timestamp_start: str = Field(..., example="2024-10-01 00:00:00")
    timestamp_end: str = Field(..., example="2024-10-30 23:59:59")

class SocialMediaAnalysisResponse(BaseModel):
    response: str

class AnalysisOnlineRequest(BaseModel):
    clipping_id: str = Field(..., example="clipping_id_1")
    timestamp_start: str = Field(..., example="2024-10-01 00:00:00")
    timestamp_end: str = Field(..., example="2024-10-30 23:59:59")

class OnlineMediaAnalysisResponse(BaseModel):
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
        api_key = x_api_key
        object_ids = payload.object_ids
        timestamp_start = payload.timestamp_start
        timestamp_end = payload.timestamp_end

        social_media_analysis_response = process_social_media_analysis_response(
            api_key=api_key,
            object_ids=object_ids,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end
        )

        if social_media_analysis_response is None:
            raise HTTPException(status_code=500, detail="No data received from social_media_analysis()")

        return {"response": social_media_analysis_response}
    except APIError as e:
        raise HTTPException(status_code=e.status_code, detail=f"Error occurred: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: exception: {e}")
        # raise HTTPException(detail=f"Error occurred: {str(e)}")


@app.post("/online-media-analysis", response_model=OnlineMediaAnalysisResponse)
def request_online_media_analysis(
    payload: AnalysisOnlineRequest, 
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

        online_media_analysis_response = process_online_media_analysis_response(
            api_key=api_key,
            clipping_id=clipping_id,
            timestamp_start=timestamp_start,
            timestamp_end=timestamp_end
        )

        if online_media_analysis_response is None:
            raise HTTPException(status_code=500, detail="No data received from online_media_analysis()")

        return {"response": online_media_analysis_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")