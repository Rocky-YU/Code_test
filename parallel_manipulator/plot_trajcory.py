#！usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = ' Rocky-YU '

'根据逆解方程来绘制满足条件的所有可达空间位置'

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
# bata = math.pi/2 # 90度
# bata = math.pi/3 # 60度
# bata = math.pi/6 # 30度
# bata = math.pi/18 # 10度
bata = 0 # 0度


# 创建点集
points =[]
col = np.random.rand(500)
print(col[1])

def condition(z):
    # 这里写你的条件
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
        # fy = math.radians(point[0])
        # alpha = math.radians(point[1])
        zp = point[2]
        q1 = func.Func(r, alpha, fy, bata, zp).q_1()
        q2 = func.Func(r, alpha, fy, bata, zp).q_2()
        q3 = func.Func(r, alpha, fy, bata, zp).q_3()
        # filtered_points.append(point)
        # 判断是否满足条件
        if 130<=q1<=160 and 130<=q2<=160 and 130<=q3<=160:
            r2 = [0,0,0,0]
            r2[0] ,r2[1] = solve_p(fy,alpha)
            r2[2] = point[2]
            r2[3] = point[3]
            filtered_points.append(r2)
            # filtered_points.append(point)
    return filtered_points

point1 = filter_points(points)
points = np.array(point1)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2],s=20,c=points[:, 3],marker='s')
ax.set_xlabel('xp')
ax.set_ylabel('yp')
ax.set_zlabel('zp')
ax.set_title(' workspace -- bata=0  ')
# ax.view_init(elev=90,azim=90) # 设置观察角度，elev表示仰角，azim表示方位角
plt.show()



