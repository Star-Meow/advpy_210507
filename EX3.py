import numpy as np
import random
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        seedcode = (sys.argv[1])
        str = list(sys.argv[2])
        num = []
        for i in range(len(str)):
            num.append(i)
        random.seed(seedcode)
        random.shuffle(num)
        enstr = []
        for i in range(len(str)):
            enstr.append(i)
        tmp = 0
        for i in num:
            enstr[tmp] = str[i]
            tmp += 1
        destr = []
        for i in range(len(str)):
            destr.append(i)
        tmp = 0        
        for i in num:
            destr[i] = enstr[tmp]
            tmp += 1

print("還原後:")
print("".join(destr))

print("加密後:")
print("".join(enstr))
