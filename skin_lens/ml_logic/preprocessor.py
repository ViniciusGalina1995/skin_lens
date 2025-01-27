from tensorflow.keras.utils import image_dataset_from_directory # type: ignore
from skin_lens.params import *

def load_data(data_dir: str):

    ds = image_dataset_from_directory(
    data_dir,
    labels="inferred",
    label_mode="categorical",
    seed=123,
    image_size=(150, 150),
    batch_size=BATCH_SIZE)

    return ds
