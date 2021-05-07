import numpy as np
import random as rand

x = np.random.randint(1, 1000,(2, 3))
fileName = "Writer.npy"
with open (fileName, "wb") as fp:
    np.save(fp, x)