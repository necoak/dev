#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b
import itertools

intext = input()
[r, g, b, n] = map(int, intext.split())

rgb_list = [r, g, b]
rgb_list.sort(reverse=True)
[x, y, z] = rgb_list

cnt = 0
for x_val in range(0, n+1, x):
    # for y_val in range(0, n+1, y):
    for y_val in range(0, (y*((n-x_val)//z))+1, y):
        zan = n - x_val - y_val
        if zan >=0 and zan % z == 0:
            cnt += 1
print(cnt)
