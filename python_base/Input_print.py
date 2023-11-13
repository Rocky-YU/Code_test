#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Rocky-YU'

def ab(a,b):
    return a*b

print('%d * %d = %d\t' %(1021,1022,ab(1021,1022)))
# 占位符 %s,%d,%f 字符串、整形、浮点型（默认为保留小数点后6位）