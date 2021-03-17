#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc139/tasks/abc139_b

a, b = map(int, input().split())

ans = 0
for i in range(21):
    i_kuti = (i-1)*(a-1) + a
    if i_kuti >=b:
        ans = i
        break

print(ans)
        
