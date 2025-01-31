from fastapi import FastAPI, UploadFile, File
from app.model import load_model, predict
from app.utils import preprocess_image

app = FastAPI()

model = load_model()

CLASS_LABELS = [
    "Actinic Keratosis", "Basal Cell Carcinoma", "Dermatofibroma", "Melanoma", "Nevus",
    "Pigmented Benign Keratosis", "Seborrheic Keratosis", "Squamous Cell Carcinoma", "Vascular Lesion"
]

@app.get("/")
def welcome():
    return {"message": "Welcome to the Skin Disease Prediction API"}

@app.post("/predict")
async def predict_skin_disease(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = preprocess_image(image_bytes)

        predictions, predicted_class_idx = predict(model, image)
        predicted_class_name = CLASS_LABELS[predicted_class_idx]
        predicted_probability = predictions[0][predicted_class_idx]
        print(f'✅✅✅Image scanned: The skin lesion is classified as {predicted_class_name} with a predicted probability of {predicted_probability * 100:.2f}%')
        return f"""
        <h1>Image scanned: The skin lesion is classified as {predicted_class_name} with a predicted probability of {predicted_probability * 100:.2f}%.</h1>
        """
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"
