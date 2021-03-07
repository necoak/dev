#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_b

n, x = list(map(int, input().split()))
a_list = list(map(int, input().split()))

ans_list = []
for a in a_list:
    if a != x:
        ans_list.append(a)

for i, ans in enumerate(ans_list):
    if i != len(ans_list):
        print(ans, end=' ')
    else:
        print(ans)
