# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
X = int(input())
if X%4 == 0: 
    if X%400 == 0:
        print('1')
    elif X%100 != 0:
        print('1')
    else:
        print('0')
else:
    print('0')
    