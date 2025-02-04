import tensorflow as tf
import os
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model_77.keras")
    model = tf.keras.models.load_model(model_path)
    print("✅ Model loaded successfully!")
    #model.save("models/model_baseline.h5")
    return model

def predict(model, preprocessed_image):
    predictions = model.predict(preprocessed_image)
    print(f'✅ {predictions}')

    predicted_class_idx = predictions.argmax(axis=1)[0]
    #return int(predicted_class_idx)
    return predictions, int(predicted_class_idx)
