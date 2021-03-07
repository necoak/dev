#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc194/tasks/abc194_d

n = int(input())

ans = 0
for i in range(n-1, 0, -1):
    ans += n / (n-i)

print(ans)

