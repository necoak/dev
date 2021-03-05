#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc087/tasks/abc087_b

from itertools import combinations

A_VAL = 500
B_VAL = 100
C_VAL = 50

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0

for a_num in range(a+1):
    for b_num in range(b+1):
        for c_num in range(c+1):
            total_val = a_num * A_VAL + b_num * B_VAL + c_num * C_VAL
            if total_val == x:
                ans += 1
print(ans)
