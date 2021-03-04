# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:30:54 2021

@author: IWTL
"""

N, X = map(int, input().split())
A = input().split()

for a in A:
    if int(a) < X:
        print(int(a), end = " ")