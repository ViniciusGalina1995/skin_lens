import os
import numpy as np

##################  VARIABLES  ##################
TRAIN_DATA_DIR = os.environ.get("TRAIN_DATA_DIR")
VAL_DATA_DIR = os.environ.get("VAL_DATA_DIR")
TEST_DATA_DIR = os.environ.get("TEST_DATA_DIR")
BATCH_SIZE = int(os.environ.get("BATCH_SIZE"))
