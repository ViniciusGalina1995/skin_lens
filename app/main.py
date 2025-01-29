# # # # main.py
# from fastapi import FastAPI, UploadFile, File
# from app.model import load_model, predict
# from app.utils import preprocess_image

# app = FastAPI()

# model = load_model()

# CLASS_LABELS = [
#     "Melanoma", "Nevus", "Basal Cell Carcinoma", "Actinic Keratosis",
#     "Pigmented Benign Keratosis", "Dermatofibroma", "Vascular Lesion", "Squamous Cell Carcinoma",
#     "Seborrheic Keratosis"
# ]

# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Skin Disease Prediction API"}

# @app.post("/predict")
# async def predict_skin_disease(file: UploadFile = File(...)):
#     try:
#         image_bytes = await file.read()

#         # Preprocess the image
#         image = preprocess_image(image_bytes)

#         # Log the shape of the image before passing it to the model
#         print(f"Image shape before model prediction: {image.shape}")

#         predicted_class_idx = predict(model, image)

#         predicted_class_name = CLASS_LABELS[predicted_class_idx]

#         return {"prediction": predicted_class_name}

#     except Exception as e:
#         return {"error": str(e)}
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
        predicted_class_idx = predict(model, image)
        print(f'✅✅✅{predicted_class_idx}')
        predicted_class_name = CLASS_LABELS[predicted_class_idx]

        return f"<h1>Predicted Disease: {predicted_class_name}</h1>"

    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"
