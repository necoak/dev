#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc165/tasks/abc165_a

import sys

input_k = input()
input_a_b = input()

k = int(input_k)
input_a, input_b = input_a_b.split()
a = int(input_a)
b = int(input_b)

xd = a // k # Divine
xm = a % k  # Amari

if xm == 0:
    print('OK')
    sys.exit(0)

if b >= k * (xd+1):
    print('OK')
    sys.exit(0)

print('NG')
sys.exit(0)
