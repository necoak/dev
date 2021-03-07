#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_a
from itertools import combinations

n = int(input())
a_list  = list(map(int, input().split()))

def calc_sajijou(tpl):
    return (tpl[0] - tpl[1]) ** 2

ans = sum(map(calc_sajijou, combinations(a_list, 2)))
print(ans)
