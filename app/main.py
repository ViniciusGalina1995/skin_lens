from fastapi import FastAPI
from pydantic import BaseModel
from api.model import load_model
from api.utils import preprocess_image
import numpy as np

app = FastAPI()
model = load_model()

# input schema for the prediction request
class ImageRequest(BaseModel):
    image: str

@app.post("/predict")
def predict(request: ImageRequest):
    image = preprocess_image(request.image)

    prediction = model.predict(image)

    return {"prediction": prediction.tolist()}
