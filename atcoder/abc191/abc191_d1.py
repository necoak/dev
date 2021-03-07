#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_d

from math import floor, ceil, sqrt
from decimal import Decimal


x0, y0, r = list(map(Decimal, input().split()))
r_square = r**2

ans = 0

# 左端,右端
x_left = x0 - r
x_right = x0 + r
x_left = ceil(x_left)
x_right = floor(x_right)

# 
for x in range(x_left, x_right+1, 1):
    
    # yの下
    y_min  = float(y0) - sqrt( (r**2) - (x-x0)**2 )
    y_max =  float(y0) + sqrt( (r**2) - (x-x0)**2 )
    #
    y_min_int = ceil(y_min)
    y_max_int = floor(y_max)
    #
    cnt = y_max_int - y_min_int + 1
    ans += cnt

print(ans)