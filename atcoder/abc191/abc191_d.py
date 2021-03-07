#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_d

from math import floor, ceil, sqrt
from _pydecimal import Decimal


x0, y0, r = list(map(Decimal, input().split()))
r_square = r**2


square_x1 = floor(x0 - r)
square_x2 = ceil(x0 + r)
square_y1 = floor(y0 - r)
square_y2 = ceil(y0 + r)

anscnt = 0
for x in range(square_x1, square_x2+1, 1):
    for y in range(square_y1, square_y2+1, 1):
        if (((x-x0)**2 + (y-y0)**2) <= r_square):
            anscnt +=1
print(anscnt)
