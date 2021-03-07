#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_a

v, t, s, d = list(map(int, input().split()))

vanish_start = v * t
vanish_end = v * s

if ((d >= vanish_start) and (d <= vanish_end)):
    print('No')
else:
    print('Yes')
