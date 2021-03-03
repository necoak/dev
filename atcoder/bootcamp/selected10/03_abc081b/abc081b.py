#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc081/tasks/abc081_b

n = int(input())
a_vals = list(map(int, input().split()))

ans = 0
while(True):
    amaris = list(map(lambda x: x%2, a_vals))
    if 1 in amaris:
        break
    a_vals = list(map(lambda x: x//2, a_vals))
    ans += 1
print(ans)

