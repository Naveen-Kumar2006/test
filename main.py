from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


# Load trained pipeline
model = joblib.load("models/price_pipeline.pkl")


# Create FastAPI application
app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices using a trained ML pipeline",
    version="1.0.0"
)


# Request schema
class HouseData(BaseModel):
    area_sqft: float
    bedrooms: int
    bathrooms: float
    stories: int
    parking: int


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "House Price Prediction API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict_price(data: HouseData):

    input_data = pd.DataFrame([{
        "area_sqft": data.area_sqft,
        "bedrooms": data.bedrooms,
        "bathrooms": data.bathrooms,
        "stories": data.stories,
        "parking": data.parking
    }])

    prediction = model.predict(input_data)

    return {
        "predicted_price": float(prediction[0])
    }