from PIL import Image
import numpy as np
import io
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.convnext import preprocess_input

def preprocess_image(image_bytes):
    """
    Preprocesses the input image for prediction by the skin disease model.
    This includes resizing the image, converting it to an array, and applying
    the preprocessor for the Transfer Learning model.
    Args:
    image_bytes (bytes): The raw bytes of the image file.
    Returns:
    numpy.ndarray: The preprocessed image array suitable for prediction.
    Raises:
    ValueError: If the image does not have the expected shape after resizing.
    """
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((224, 224))
    image_array = img_to_array(image)

    ########### add the preprocessor of the Transfer Learning model we use!!!!!

    if image_array.shape != (224, 224, 3):
        raise ValueError(f"Input image must have shape (224, 224, 3), but got {image_array.shape}.")

    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)
    print(f"✅Processed image shape: {image_array.shape}")

    return image_array
