#!usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module'
__author__ = 'Rocky-Yu'
import math
s= 'song'

def quadratic(a, b, c):
    for i in (a,b,c):
        if not isinstance(i,(float,int)):
            raise TypeError('输入的参数不符合规范')

    if (b*b-(4*a*c)) >=0:
        # egien = math.sqrt(b * b - (4 * a * c))
        egien = math.sqrt(b ** 2 - (4 * a * c))
        # b**2 表示b的平方
        egien_1 = (-b + egien) / (2 * a)
        egien_2 = (-b - egien) / (2 * a)
        print('方程 %dx2 + %dbx + %d = 0 的根为\t',egien_1,'\t',egien_2)
    elif (b * b - (4 * a * c)) < 0:
        egien = math.sqrt(abs(b * b - (4 * a * c)))
        egien_b = (-b ) / (2 * a)
        egien_1 = egien / (2 * a)
        print('方程 %dx2 + %dbx + %d = 0 根为一对虚根\t', '%d + %di\t'%(egien_b, egien_1),'%d - %di'%(egien_b, egien_1))

quadratic(2,1,0)
quadratic(2,5,6)
quadratic(2,5,s)