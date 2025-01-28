from skin_lens.ml_logic.preprocessor import load_data
from skin_lens.params import *

def preprocess():
    """
    - Load data from local directory
    - Process data ()
    - Store processed data on your personal BQ (truncate existing table if it exists)
    - No need to cache processed data as CSV (it will be cached when queried back from BQ during training)
    """
    train_ds = load_data(TRAIN_DATA_DIR)
    val_ds = load_data(VAL_DATA_DIR)
    test_ds = load_data(TEST_DATA_DIR)

    print('✅ loading data successful!')
    print(f"The Train Data has {len(train_ds.class_names)} classes")
    print(f"The Val Data has {len(val_ds.class_names)} classes")
    print(f"The Test Data has {len(test_ds.class_names)} classes")

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
