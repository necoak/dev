#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc060/tasks/abc060_b

import sys

a, b, c = map(int, input().split())

for i in range(1, b+1):
    if (((a * i) % b) == c):
        print('YES')
        sys.exit(0)
print('NO')
