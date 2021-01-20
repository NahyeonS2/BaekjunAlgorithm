# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = int(input())
b = int(input())
A = a//100
B = (a-A*100)//10
C = a-A*100-B*10
D = b//100
E = (b-D*100)//10
F = b-D*100-E*10

print( a*F )
print( a*E )
print( a*D )
print( a*F + a*E*10 + a*D*100 )