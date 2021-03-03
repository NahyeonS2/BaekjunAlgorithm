# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:00:34 2021

@author: IWTL
"""

T = int(input())

for t in range(1,T+1):
    A, B = map(int, input().split())
    print("Case #%d:"%t, A+B)