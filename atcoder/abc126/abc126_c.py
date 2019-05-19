#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc126/tasks/abc126_c
from math import log2,ceil

intext1 = input()
[n, k] = map(int, intext1.split())

kakuritu = 0.0
for v in range(1, n+1):
    if v >= k:
        tmp_kakuritu = 1 / n
        kakuritu += tmp_kakuritu
    else:
        x = ceil(log2(k/v))
        #
        tmp_kakuritu = 1 / n / 2**x
        kakuritu += tmp_kakuritu

print(kakuritu)
