#!Anaconda/anaconda/python
#coding: utf-8

import numpy as np

# numpy 中包含两种基本的数据类型：数组、矩阵

# 一维数组
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(a1 + a2)
print(a1*a2)
print(a1*2)
print(a1**2)

print('-------------------------------')

# 多维数组
aa1 = np.array([[1,2,3], [4,5,6]])
print(aa1[0])
print(aa1[0][0], ' as well as ', aa1[0,0])

# numpy中还有很多用来直接创建数组的函数，和MATLAB中类似
# 比如： zeros, ones, full, eye, random.random



print('-------------------------------')

# 矩阵
m1 = np.mat([1,2,3])
m2 = np.mat([1,2,3]).T
print(m1)
print(m2)

# 输出矩阵一整行
print(m1[0])
print(m1[0,0])

# 矩阵乘法，行 x 列
print(m1*m2)
# 矩阵点乘，对应元素相乘
print(np.multiply(m1,m2.T))