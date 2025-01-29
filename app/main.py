from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model
from app.utils import preprocess_image
import numpy as np

app = FastAPI()
model = load_model()

# input schema for the prediction request
#class ImageRequest(BaseModel):
#    image: str

@app.get("/")
def index():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: ImageRequest):
    image = preprocess_image(request.image)

    prediction = model.predict(image)

    return {"prediction": prediction.tolist()}
