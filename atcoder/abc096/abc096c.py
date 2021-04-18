#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc096/tasks/abc096_c

import sys

H, W = list(map(int, input().split()))
s = []
for _ in range(H):
    s.append(list(input()))

for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            continue
        if (i-1 >= 0) and (s[i-1][j]=='#'):
            continue
        elif (i+1 < H) and (s[i+1][j]=='#'):
            continue
        elif (j-1 >= 0) and (s[i][j-1] =='#'):
            continue
        elif (j+1 < W) and (s[i][j+1]=='#'):
            continue
        print('No')
        sys.exit(0)
print('Yes')
