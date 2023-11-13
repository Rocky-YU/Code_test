#!usr/bin/env python3
# -*- coding: utf-8 -*-
' a imu test module'
__author__ = 'Rocky-Yu'

import math
from time import sleep
import numpy

# Import sensor data ("short_walk.csv" or "long_walk.csv")
data = numpy.genfromtxt("tag.csv", delimiter=",", skip_header=1)
sample_rate = 200  # 400 Hz
timestamp = data[:, 0]
accelerometer = data[:, 1:4]
gyroscope = data[:, 4:7]



class IMU():
    def __init__(self,gyroscope,accelerometer):

        self.gyroscope = gyroscope
        self.accelerometer = accelerometer
        print("[IMU] Initialised.")
    
    # rad/s
    def get_gyro_bias(self, N=100):
        bx = 0.0
        by = 0.0
        bz = 0.0

        for i in range(N):
            [gx, gy, gz] = self.get_gyro(i)
            bx += gx
            by += gy
            bz += gz
            sleep(0.01)

        return [bx / float(N), by / float(N), bz / float(N)]
        
    # rad/s
    def get_gyro(self,i):
        gx = self.gyroscope[i,0]
        gy = self.gyroscope[i,1]
        gz = self.gyroscope[i,2]
        return [gx, gy, gz]        
        
    # m/s^2
    def get_acc(self,i):
        ax = self.accelerometer[i,0]
        ay = self.accelerometer[i,1]
        az = self.accelerometer[i,2]
        return [ax, ay, az]
    
    # rad
    def get_acc_angles(self,i):
        [ax, ay, az] = self.get_acc(i)
        phi = math.atan2(ay, math.sqrt(ax ** 2.0 + az ** 2.0))
        theta = math.atan2(-ax, math.sqrt(ay ** 2.0 + az ** 2.0))
        return [phi, theta]

        
