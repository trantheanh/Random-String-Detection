import tensorflow as tf
import tensorflow.keras as keras

import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# data = pd.read_csv("data.csv", header=None)
# data[0] = data[0].str.lower()
# data = data.drop_duplicates()
# data.to_csv("non_duplicate_data.csv")
data = pd.read_csv("non_duplicate_data.csv", header=None)
data = data.values[2:, 2]
# print(data[:5])
data = (data != "LEGIT").astype(np.int)
plt.hist(data, bins=2)
plt.show()
