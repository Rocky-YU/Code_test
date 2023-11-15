#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'Rocky-YU'

def ab(a,b):
    return a*b

print('%d * %d = %d\t' %(1021,1022,ab(1021,1022)))
# 占位符 %s,%d,%f 字符串、整形、浮点型（默认为保留小数点后6位）

def input_ab():
    number = input('请输入两个作乘法运算的数')
    array = list(int(char) for char in number.split(','))
    #使用 str.split() 方法将字符串转换为数组，例如 array = string.split(',') or array = string.split(' ')
    # str.split() 方法将在每次出现提供的分隔符时将字符串拆分为一个列表
    number_ab = ab(array[1],array[0])
    print('您输入的两个数：%s 和 %s ' %(array[1],array[0]) +'的乘法结果=' '%d' %number_ab)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n,'\t',f,'\t',s1,'\n',s2)
print(s3,'\t',s4,'\t')

n_16 = hex(n)
print('%d 的十六进制为：'%n, n_16)

