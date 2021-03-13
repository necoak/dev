#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_b

CANT_STR='UNSATISFIABLE'

a,b,w = list(map(int, input().split()))
w = w*1000

import math
b_ko = math.ceil(w / b)
a_ko = math.floor(w / a)

if b_ko > a_ko:
    print(CANT_STR)
else:
    print(b_ko, a_ko)
