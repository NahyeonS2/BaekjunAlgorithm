# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:47:59 2021

@author: IWTL
"""
import sys
T = int(sys.stdin.readline())
for t in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)