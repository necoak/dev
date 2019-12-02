#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/agc040/tasks/agc040_a

s = input()
a = [0] * (len(s) + 1)

for i in range(0, len(s)):
    if (s[i] == '<'):
        a[i+1] = a[i] + 1
for i in range(len(s)-1, -1, -1):
    if (s[i] == '>'):
        a[i] = max(a[i], a[i+1]+1)
#print(a)
print(sum(a))

