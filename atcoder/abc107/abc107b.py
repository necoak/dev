#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc107/tasks/abc107_b

H, W = list(map(int, input().split()))

a = []
for i in range(H):
    a.append(list(input()))

to_delete_gyo =  []
for gyo in range(H):
    is_all_white = True
    for retu in range(W):
        if a[gyo][retu] == '#':
            is_all_white = False
            break
    if is_all_white:
        to_delete_gyo.append(gyo)

to_delete_retu =  []
for retu in range(W):
    is_all_white = True
    for gyo in range(H):
        if a[gyo][retu] == '#':
            is_all_white = False
            break
    if is_all_white:
        to_delete_retu.append(retu)

for i in range(H):
    if i in to_delete_gyo:
        continue
    for j in range(W):
        if j in to_delete_retu:
            continue
        
        print(a[i][j], end='')
    print('')
