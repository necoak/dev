#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc098/tasks/abc098_b

n = int(input())
s = input()
ans = 0

for cut_indx in range(n):
    s1 = set(s[:cut_indx])
    s2 = set(s[cut_indx:])
    s1_and_s2_size = len(s1 & s2)
    if s1_and_s2_size > ans:
        ans = s1_and_s2_size

print(ans)