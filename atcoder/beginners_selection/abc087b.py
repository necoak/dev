#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc087_b
import itertools

a = int(input())
b = int(input())
c = int(input())
x = int(input())

a_patterns = []
b_patterns = []
c_patterns = []

# A : 500円パターン
for ax in range(0, a+1, 1):
    a_patterns.append(ax * 500)

# B : 100円パターン
for bx in range(0, b+1, 1):
    b_patterns.append(bx * 100)

# C : 50円パターン
for cx in range(0, c+1, 1):
    c_patterns.append(cx * 50)

ok_pattern_num = 0

abc_patterns = itertools.product(a_patterns, b_patterns, c_patterns)
for abc_pattern in abc_patterns:
    abc = abc_pattern[0] + abc_pattern[1] + abc_pattern[2]
    if abc == x:
        ok_pattern_num += 1
print(ok_pattern_num)

