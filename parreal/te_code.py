import numpy as np

# 创建两个矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 使用NumPy的dot函数进行矩阵乘法
C = np.dot(A, B)

# 打印结果
print("矩阵A：")
print(A)
print("矩阵B：")
print(B)
print("矩阵A和矩阵B的乘积：")
print(C)