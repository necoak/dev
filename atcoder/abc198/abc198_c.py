#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc198/tasks/abc198_c
import sys
from math import ceil, sqrt

R, X, Y = list(map(int, input().split()))

distance = sqrt(X**2 + Y**2)

ans = None
if R > distance:
    ans = 2
else:
    ans = ceil(distance / R)
print(ans)
