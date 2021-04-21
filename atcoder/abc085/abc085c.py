#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc085_b

import sys

N, Y = list(map(int, input().split()))

BILLS = [1000, 5000, 10000]

for i in range(N+1):
    for j in range(0, N+1-i):
        k = N - i - j
        if (10000*i + 5000*j + 1000*k) == Y:
            print(i, j, k)
            sys.exit(0)
print(-1, -1, -1)
