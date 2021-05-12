import numpy as np
import random
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        seedcode = (sys.argv[1])
        data = list(sys.argv[2])
        datalist = []
        for i in range(len(data)):
            datalist.append(i)
        



random.seed(seedcode)
random.shuffle(data)
random.shuffle(datalist)


print("加密前:")
print(datalist)

print("加密後:")
print("".join(data))
print(data)