# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:59:43 2024

@author: DiemKieu
"""
import math
a=float(input("a:"))
b=float(input("b:"))
x1=(math.pow(a,1/2)-math.pow(b,1/2))/(math.pow(a,1/4)-math.pow(b,1/4))
x2=(math.pow(a,1/2)+math.pow(a*b,1/4))/(math.pow(a,1/4)+math.pow(b,1/4))
print(f"{x1}-{x2}")
                      