#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_b
import itertools

intext = input()
[r, g, b, n] = map(int, intext.split())

r_list = [rn for rn in range(0, n+1, r)]
g_list = [gn for gn in range(0, n+1, g)]
b_list = [bn for bn in range(0, n+1, b)]

rgb_combis = itertools.product(r_list, g_list, b_list)

cnt = 0
for rn, gn, bn in rgb_combis:
    if (rn+gn+bn) == n:
        cnt +=1

print(cnt)