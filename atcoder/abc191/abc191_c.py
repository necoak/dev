#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_a
from collections import defaultdict

h, w = list(map(int, input().split()))

s = defaultdict(str)

for i in range(h):
    gyo_j = list(input())
    for j, sij in enumerate(gyo_j):
        s[(i,j)] = sij

kakukei = 0
for i in range(h):
    for j in range(w):
        cnt = 0
        if s[(i,j)] == '#':
            cnt += 1
        if s[(i,j+1)] == '#':
            cnt += 1
        if s[(i+1,j)] == '#':
            cnt += 1
        if s[(i+1,j+1)] == '#':
            cnt += 1
        if ((cnt==1)or(cnt==3)):
            kakukei += 1
        
print(kakukei)
