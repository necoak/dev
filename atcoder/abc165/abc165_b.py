#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc165/tasks/abc165_b
import math

input_x = input()
x = int(input_x)

zandaka = 100
nen = 0

while zandaka < x:
    nen += 1
    zandaka = math.floor(zandaka * 1.01)

print(nen)
