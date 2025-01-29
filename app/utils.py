import numpy as np
from PIL import Image
import io

def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    # adjust to 128x128 or 224x224
    image = image.resize((128, 128))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# import io
# import numpy as np
# from PIL import Image
# import base64

# def preprocess_image(image_str: str):
#     image_bytes = base64.b64decode(image_str)

#     image = Image.open(io.BytesIO(image_bytes))

#     image = image.resize((128, 128))
#     image = np.array(image) / 255.0
#     image = np.expand_dims(image, axis=0)
#     return image
