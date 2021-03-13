#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_a

import sys

n = int(input())
v = 1
keta_cnt = 0
keta = 0

if n < 1000:
    print('0')
    sys.exit(0)

while(True):

    keta += 1
    v = v*1000
    if n >= v*1000:
        keta_cnt += keta * (v*1000 - v)
    else:
        keta_cnt += keta * (n - v + 1)
        break

print(keta_cnt)