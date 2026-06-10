from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib



# FastAPI App


app = FastAPI(
    title="Uber Fare Estimator API",
    description="Predict Uber/Ola fare using Machine Learning",
    version="1.0.0"
)



# Model Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR /
    "Models" /
    "uber_fare_model.pkl"
)



# Load Model

model = joblib.load(
    r"..\Models\uber_fare_model.pkl"
)


# Request Schema


class FareRequest(BaseModel):
    passenger_count: int = Field(..., ge=1, le=8)
    hour: int = Field(..., ge=0, le=23)
    day: int = Field(..., ge=1, le=31)
    month: int = Field(..., ge=1, le=12)
    weekday: int = Field(..., ge=0, le=6)
    distance: float = Field(..., gt=0, le=100)



# # Response Schema


class FareResponse(BaseModel):
    predicted_fare: float



# Home Endpoint


@app.get("/")
def home():
    return {
        "message": "Uber Fare Estimator API is Running 🚕"
    }



# Health Check


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }



# Prediction Endpoint


@app.post(
    "/predict",
    response_model=FareResponse
)
def predict_fare(data: FareRequest):

    input_data = pd.DataFrame(
        [[
            data.passenger_count,
            data.hour,
            data.day,
            data.month,
            data.weekday,
            data.distance
        ]],
        columns=[
            "passenger_count",
            "hour",
            "day",
            "month",
            "weekday",
            "distance"
        ]
    )

    prediction = model.predict(input_data)[0]

    return FareResponse(
        predicted_fare=round(
            float(prediction),
            2
        )
    )