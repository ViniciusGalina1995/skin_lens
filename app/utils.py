from PIL import Image
import numpy as np
import io

import tensorflow as tf


def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize((150, 150))
    image_array = tf.keras.preprocessing.image.img_to_array(image)

    if image_array.shape != (150, 150, 3):
        raise ValueError(f"Input image must have shape (150, 150, 3), but got {image_array.shape}.")

    image_array = np.expand_dims(image_array, axis=0)

    print(f"✅Processed image shape: {image_array.shape}")

    return image_array
