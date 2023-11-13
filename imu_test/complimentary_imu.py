#!usr/bin/env python3
# -*- coding: utf-8 -*-
' a imu test module'

__author__ = 'Rocky-Yu'

import numpy as np
from imu import *
from time import time
from math import sin, cos, tan, pi

data = np.genfromtxt("tag.csv", delimiter=",", skip_header=1)
sample_rate = 200  # 400 Hz
timestamp = data[:, 0]
accelerometer = data[:, 1:4]
gyroscope = data[:, 4:7]

imu = IMU(gyroscope,accelerometer)

N = len(timestamp)
# Filter coefficient
alpha = 0.1

print("Calculating average gyro bias...")
[bx, by, bz] = imu.get_gyro_bias(1000)

# Complimentary filter estimates
phi_hat = 0.0
theta_hat = 0.0

print("Running...")

# Measured sampling time
dt = 0.0

for i in range(N-1):
    dt = timestamp[i+1] - timestamp[i]
    # Get estimated angles from raw accelerometer data
    [phi_hat_acc, theta_hat_acc] = imu.get_acc_angles(i)
    
    # Get raw gyro data and subtract biases
    [p, q, r] = imu.get_gyro(i)
    p -= bx
    q -= by
    r -= bz
    
    # Calculate Euler angle derivatives 
    phi_dot = p + sin(phi_hat) * tan(theta_hat) * q + cos(phi_hat) * tan(theta_hat) * r
    theta_dot = cos(phi_hat) * q - sin(phi_hat) * r
    
    # Update complimentary filter
    phi_hat = (1 - alpha) * (phi_hat + dt * phi_dot) + alpha * phi_hat_acc
    theta_hat = (1 - alpha) * (theta_hat + dt * theta_dot) + alpha * theta_hat_acc   
    
    # Display results
    print("Phi: " + str(np.round(phi_hat * 180.0 / pi, 1)) + " | Theta: " + str(np.round(theta_hat * 180.0 / pi, 1)))

