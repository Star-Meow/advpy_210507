import numpy as np
import random

np.random.seed
x1 = np.random.randint(1, 1000,(2, 3))
fileName = "Writer.npy"
with open(fileName, "rb") as fp:
    np.save(fp, x1)