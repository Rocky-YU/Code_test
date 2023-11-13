import numpy as np
import matplotlib.pyplot as plt

# 输入IMU数据
time = [0.1, 0.2, 0.3, 0.4, 0.5]  # 时间序列
gx = [0.1, 0.2, 0.3, 0.4, 0.5]  # 陀螺仪x轴数据
gy = [0.2, 0.3, 0.4, 0.5, 0.6]  # 陀螺仪y轴数据
gz = [0.3, 0.4, 0.5, 0.6, 0.7]  # 陀螺仪z轴数据
ax = [0.4, 0.5, 0.6, 0.7, 0.8]  # 加速度计x轴数据
ay = [0.5, 0.6, 0.7, 0.8, 0.9]  # 加速度计y轴数据
az = [0.6, 0.7, 0.8, 0.9, 1.0]  # 加速度计z轴数据

# 预积分计算轨迹
dt = np.diff(time)  # 计算时间间隔
omega = np.array([gx, gy, gz])  # 陀螺仪角速度
acc = np.array([ax, ay, az])  # 加速度计加速度

# 预积分
position = np.zeros((3, len(time)))  # 位置矩阵
velocity = np.zeros((3, len(time)))  # 速度矩阵
orientation = np.zeros((3, len(time)))  # 姿态矩阵

for i in range(1, len(time)):
    # 更新姿态
    orientation[:, i] = orientation[:, i - 1] + omega[:, i - 1] * dt[i - 1]

    # 更新速度
    velocity[:, i] = velocity[:, i - 1] + acc[:, i - 1] * dt[i - 1]

    # 更新位置
    position[:, i] = position[:, i - 1] + velocity[:, i - 1] * dt[i - 1]

# 绘制轨迹
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(position[0], position[1], position[2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
