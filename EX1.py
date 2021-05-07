import numpy as np
import random as rand

x = np.ones((2, 3, 4)) * 128
# 建立2*3*4全為1*128的陣列

np.zeros((2 , 3))
# 建立2*3全為0的陣列

np.arange(1, 10, 2)
# 建立1開始不超過10間隔值為2的均勻數值的陣列

np.linspace(0, 10, 5)
#建立0~10間 均勻的五個數值陣列

y = np.random.randint(1, 100, (2 , 3))
#1~100 隨機 2*3陣列

z = y.reshape(1 , 6)
#陣列重新排序成1*6
z.sort()
#z陣列進去由大到小排出來

'''
data = list("This is a booK")
print(data)
rand.seed(1723)
rand.shuffle(data)
print("".join(data))
'''