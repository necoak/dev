#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc198/tasks/abc198_b

import sys
N = input()

for i in range(10):
    tmp_N = '0'*i + N
    if tmp_N == tmp_N[::-1]:
        print('Yes')
        sys.exit(0)
print('No')
