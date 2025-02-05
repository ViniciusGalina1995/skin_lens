import tensorflow as tf
import os
def load_model():
    """
    Loads and returns the trained skin disease prediction model.

    The model is loaded from the specified file path.

    Returns:
    tf.keras.Model: The loaded Keras model.
    """
    model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model_77.keras")
    model = tf.keras.models.load_model(model_path)
    print("✅ Model loaded successfully!")
    #model.save("models/model_baseline.h5")
    return model

def predict(model, preprocessed_image):
    """
    Predicts the class of the skin lesion from the preprocessed image using the model.

    Args:
    model (tf.keras.Model): The loaded Keras model.
    preprocessed_image (numpy.ndarray): The preprocessed image suitable for prediction.

    Returns:
    tuple: A tuple containing the prediction array and the predicted class index.
    """
    predictions = model.predict(preprocessed_image)
    print(f'✅ {predictions}')

    predicted_class_idx = predictions.argmax(axis=1)[0]
    #return int(predicted_class_idx)
    return predictions, int(predicted_class_idx)
