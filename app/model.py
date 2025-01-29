# # model.py
import tensorflow as tf

# def load_model():
#     # Load the trained model
#     model = tf.keras.models.load_model("models/model_baseline.keras")
#     return model

# def predict(model, preprocessed_image):
#     # Predict class using the model
#     predictions = model.predict(preprocessed_image)
#     predicted_class = predictions.argmax(axis=1)[0]  # Get class index
#     return predicted_class
import tensorflow as tf
import os
import numpy as np
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model_baseline.keras")
    model = tf.keras.models.load_model(model_path)
    print("✅ Model loaded successfully!")
    #model.save("models/model_baseline.h5")

    return model

def predict(model, preprocessed_image):
    predictions = model.predict(preprocessed_image)
    print(f'✅ {predictions}')

    predicted_class_idx = predictions.argmax(axis=1)[0]
    return int(predicted_class_idx)
