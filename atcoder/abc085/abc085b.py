#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc085_b

N = int(input())
d_list = []
for i in range(N):
    d_list.append(int(input()))

print(len(set(d_list)))
