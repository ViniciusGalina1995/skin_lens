from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from app.model import load_model, predict
from app.utils import preprocess_image

app = FastAPI()

model = load_model()

CLASS_LABELS = [
    "Actinic Keratosis","Basal Cell Carcinoma", "Dermatofibroma", "Melanoma", "Nevus",
    "Pigmented Benign Keratosis", "Seborrheic Keratosis", "Squamous Cell Carcinoma", "Vascular Lesion"

]

@app.get("/", response_class=HTMLResponse)
def upload_form():
    return """
    <html>
        <body>
            <h2>Upload a Skin Image for Prediction</h2>
            <form action="/predict" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*" required>
                <button type="submit">Predict</button>
            </form>
        </body>
    </html>
    """

@app.post("/predict", response_class=HTMLResponse)
async def predict_skin_disease(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = preprocess_image(image_bytes)

        predictions, predicted_class_idx = predict(model, image)

        predicted_class_name = CLASS_LABELS[predicted_class_idx]
        predicted_probability = predictions[0][predicted_class_idx]

        print(f'✅✅✅Image scanned: The skin lesion is classified as {predicted_class_name} with a predicted probability of {predicted_probability * 100:.2f}%')
        #print(f'✅✅✅ Confidence: {predicted_probability * 100:.2f}%')

        return f"""
        <h1>Image scanned: The skin lesion is classified as {predicted_class_name} with a predicted probability of {predicted_probability * 100:.2f}%.</h1>

        """
        # probabilities_text = "<br>".join(
        #     [f"{CLASS_LABELS[i]}: {prob:.4f}" for i, prob in enumerate(predictions[0])]
        # )

        # return f"""
        # <h1>Predicted Disease: {predicted_class_name}</h1>
        # <h2>Prediction Probabilities:</h2>
        # <p>{probabilities_text}</p>
        # """
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"
