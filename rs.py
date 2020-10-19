import tensorflow as tf
import tensorflow.keras as keras

import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv", header=None).values[1:, 1]
# print(len(data))
# data = set([example.lower() for example in data])
# print(len(data))
# lens = np.array([len(example)for example in data])
data = (data != "LEGIT").astype(np.int)
plt.hist(data, bins=2)
plt.show()
