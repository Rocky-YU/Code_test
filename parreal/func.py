#! usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Rocky-YU'
' 基于并联机构的正解求反解，获得各主动运动关节的运动量'

import math
# r = 100 # 单位为 mm
# bata = math.radians(30) # 30度
# fy = 10
# bata = 10
# zp = 20
class Func():

    def __init__(self,r,alpha,fy,bata,zp):
        self.r = r
        self.alpha = alpha
        self.fy = fy
        self.bata = bata
        self.zp = zp

    def q_1(self):
        # math.sin(弧度)  # 假设𝛼为60度  # alpha = math.radians(60)
        q1 = self.zp + self.r * (1 - (math.sqrt(3)/2)*math.sin(2*self.alpha)*(1-math.cos(self.fy)) - (math.cos(self.alpha)**2)
                       - math.cos(self.fy)*(math.sin(self.alpha)**2))*math.tan(self.bata) + self.r*math.sin(self.fy)*math.sin(self.alpha - math.pi/6)
        return q1

    def q_2(self):
        # math.sin(弧度)  # 假设𝛼为60度  # alpha = math.radians(60)
        q2 = self.zp + self.r * (1 + (1/2)*math.cos(2*self.alpha)*(1-math.cos(self.fy)) - (math.sin(self.alpha)**2)
                       - math.cos(self.fy)*(math.cos(self.alpha)**2))*math.tan(self.bata) + self.r*math.sin(self.fy)*math.cos(self.alpha)
        return q2

    def q_3(self):
        # math.sin(弧度)  # 假设𝛼为60度  # alpha = math.radians(60)
        q3 = self.zp + self.r * (1 + ((math.sqrt(3)/2)*math.sin(2*self.alpha)*(1-math.cos(self.fy))) - (math.cos(self.alpha)**2)
                       - math.cos(self.fy)*(math.sin(self.alpha)**2))*math.tan(self.bata) - self.r*math.sin(self.fy)*math.sin(self.alpha + math.pi/6)
        return q3


# func = Func(r,bata,fy,bata,zp)
# q11 = func.q_1()
# print(q11)
