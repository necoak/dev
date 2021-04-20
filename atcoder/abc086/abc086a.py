#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc086_a

a, b = list(map(int, input().split()))

if (a * b) % 2 == 0:
    print('Even')
else:
    print('Odd')
