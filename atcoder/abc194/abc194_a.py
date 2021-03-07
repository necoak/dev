#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc194/tasks/abc194_a

a, b = list(map(int, input().split()))

if (a+b) >= 15 and b >=8:
    print(1)
elif (a+b) >= 10 and b >= 3:
    print(2)
elif a+b >= 3:
    print(3)
else:
    print(4)
