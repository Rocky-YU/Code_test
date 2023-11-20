#！usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = ' Rocky-YU '

'根据雅克比矩阵计算条件数'

import random
import func
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义初始模型条件
r = 100 # 单位为 mm
# bata = math.pi/1.5 # 120度
bata = math.radians(50)
# bata = math.pi/2 # 90度
# bata = math.pi/3 # 60度
# bata = math.pi/6 # 30度
# bata = math.pi/18 # 10度
# bata = 0.001 # 0度

# 创建点集
points =[]
col = np.random.rand(500)
print(col[1])

def condition(z):
    # 这里写你的条件，例如：
    return col[int((z-130))]

for z in np.arange(130, 160, 1):
    for x in np.arange(0, math.pi,0.02):
        for y in np.arange(0, 2*math.pi,0.04):
            # print(f'({x}, {y}, {z})')
            r2 = [0, 0, 0, 0]
            # r1 = math.sqrt(fy**2 + zp**2)
            r2[0] = x
            r2[1] = y
            r2[2] = z
            r2[3] = condition(z)
            points.append(r2)

# 求解动平台中心坐标
def solve_p(fy,alpha):
    xp = (-100)*math.cos(alpha)*math.sin(alpha)*(1-math.cos(fy))
    yp = 50*((math.cos(alpha)**2)-(math.sin(alpha)**2))*(1-math.cos(fy))
    return xp,yp



def filter_points(points):
    filtered_points = []
    for point in points:
        # 计算点到原点的距离
        fy = point[0]
        alpha = point[1]
        zp = point[2]
        q1 = func.Func(r, alpha, fy, bata, zp).q_1()
        q2 = func.Func(r, alpha, fy, bata, zp).q_2()
        q3 = func.Func(r, alpha, fy, bata, zp).q_3()
        if 130<=q1<=160 and 130<=q2<=160 and 130<=q3<=160:
            if point[2]==140 and point[0] > 0 and point[1] > 0:
                J_1 = func.Func(r, alpha, fy, bata=bata).j_c_1()
                J = np.linalg.inv(J_1)
                # 计算雅可比矩阵的条件数
                # condition_number = np.linalg.cond(J)
                matrix_norm = np.linalg.norm(J, ord=2)
                # 计算矩阵的逆矩阵
                inverse_matrix = np.linalg.inv(J)
                # 计算逆矩阵的谱范数
                inverse_matrix_norm = np.linalg.norm(inverse_matrix, ord=2)
                # 计算条件数
                condition_number = matrix_norm * inverse_matrix_norm
                r2 = [0, 0, 0, 0]
                r2[0], r2[1] = solve_p(fy, alpha)
                r2[2] = point[2]
                r2[3] = 1/condition_number
                filtered_points.append(r2)
                # filtered_points.append(point)
        # fy = math.radians(point[0])
        # alpha = math.radians(point[1])
        # 求矩阵的转置
        # J_1_T = np.transpose(J_1)
        # # 求矩阵的逆
        # J = np.linalg.inv(J_1)
        # J_T = np.transpose(J)
        # # 求矩阵的迹
        # trj_J_T = np.trace(np.dot(J, J_T))
        # C_J = math.sqrt(trj_J_T) + math.sqrt(trj_J_T)
        # filtered_points.append(point)

    return filtered_points

point1 = filter_points(points)
points = np.array(point1)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(points[:, 0], points[:, 1],points[:, 2],s=20,c=points[:, 3],marker='s')
# ax.set_xlabel('xp')
# ax.set_ylabel('yp')
# ax.set_zlabel('zp')
# ax.set_title(' condition_number ')
# plt.colorbar()
# ax.view_init(elev=90,azim=90)
plt.scatter(points[:, 0], points[:, 1],s=20,c=points[:, 3],marker='s')
plt.xlabel('xp')
plt.ylabel('yp')
plt.title(' condition_number_zp=140_bata=50 ')
plt.colorbar()
plt.show()

# ax.view_init(elev=0, azim=90)  # 设置观察角度，elev表示仰角，azim表示方位角
# plt.savefig('front_view.png')  # 保存图像为front_view.png
# plt.show()

