#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_a

m, h = list(map(int, input().split()))

if h % m == 0:
    print('Yes')
else:
    print('No')
