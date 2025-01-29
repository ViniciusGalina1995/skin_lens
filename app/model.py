import tensorflow as tf

def load_model():
    # CNN model
    model = tf.keras.models.load_model("model/model.h5")
    return model

def predict(model, preprocessed_image):
    predictions = model.predict(preprocessed_image)
    predicted_class = predictions.argmax(axis=1)[0]
    return predicted_class
