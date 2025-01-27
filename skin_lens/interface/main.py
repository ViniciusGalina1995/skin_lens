from skin_lens.ml_logic.preprocessor import load_data
from skin_lens.params import *

def preprocess():
    train_ds = load_data(TRAIN_DATA_DIR)
    val_ds = load_data(VAL_DATA_DIR)
    test_ds = load_data(TEST_DATA_DIR)
    


if __name__ == '__main__':
    print(TEST_DATA_DIR)
    try:
        pass
    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
