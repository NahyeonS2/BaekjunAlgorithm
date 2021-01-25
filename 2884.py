# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
h , m = map(int, input().split())

if m >= 45 :
    print (h, (m-45))
elif m < 45 :
    if h != 0 :
        print ((h-1), (m+15))
    else :
        print ('23', (m+15))