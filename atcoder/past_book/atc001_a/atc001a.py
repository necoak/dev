#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(500*500)

H,W = list(map(int, input().split()))
c = []
for _ in range(H):
    c.append(list(input()))

s_i = -1
s_j = -1
for i in range(H):
    for j in range(W):
        if (c[i][j] == 's'):
            s_i = i
            s_j = j

visited = []
for _ in range(H):
    visited.append([False for x in range(W)])

def dfs(i, j):
    visited[i][j] = True
    if (c[i][j] == 'g'):
        print('Yes')
        sys.exit(0)
            
    # go Next
    next_ij_list = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for next_i, next_j in next_ij_list:
        if ((0 <= next_i < H) and
            (0 <= next_j < W) and
            (c[next_i][next_j] != '#') and 
            (visited[next_i][next_j] == False)):
            dfs(next_i, next_j)
    # visited[i][j] = False
    return

dfs(s_i, s_j)

print('No')

