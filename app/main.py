from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field


MODEL_PATH = Path(__file__).resolve().parent.parent / "model.joblib"

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="ML Inference API",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=4,
        max_length=4
    )


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(request: PredictionRequest):
    probabilities = model.predict_proba([request.features])[0]
    prediction = model.predict([request.features])[0]

    return {
        "prediction": int(prediction),
        "confidence": round(float(max(probabilities)), 4)
    }