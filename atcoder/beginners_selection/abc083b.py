#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc083_b
import itertools

def get_keta_list(v):
    keta_list = []
    while v != 0:
        keta_list.append(v %10)
        v = v // 10
    return keta_list


n_a_b_text = input()
[n, a, b] = map(int, n_a_b_text.split())

vlist = []
for v in range(n+1):
    v_ketasum = sum(get_keta_list(v))
    if a <= v_ketasum <= b:
        vlist.append(v)

print(sum(vlist))
