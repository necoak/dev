#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc083/tasks/abc083_b

n, a, b = list(map(int, input().split()))

def calc_ketawa(val):
    retval = 0
    tmp_val = val
    while tmp_val >= 10:
        retval += (tmp_val % 10)
        tmp_val = tmp_val // 10
    retval += tmp_val
    return retval

ans = 0
for x in range(1, n+1, 1):
    x_ketawa =calc_ketawa(x)
    if x_ketawa >= a and x_ketawa <= b:
        ans += x
print(ans)
