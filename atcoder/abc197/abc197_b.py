#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc196/tasks/abc196_b

H, W, X, Y = list(map(int, input().split()))

masu = []
for i in range(H):
    si = input()
    masu.append(list(si))

viewpoint_x = X-1
viewpoint_y = Y-1

ans = 1

# Ue
target_y = viewpoint_y
for target_x in range(viewpoint_x-1, -1,-1):
    if masu[target_x][target_y] == '#':
        break
    ans += 1

# Down
target_y = viewpoint_y
for target_x in range(viewpoint_x+1, H, 1):
    if masu[target_x][target_y] == '#':
        break
    ans += 1

# Left
target_x = viewpoint_x
for target_y in range(viewpoint_y-1, -1, -1):
    if masu[target_x][target_y] == '#':
        break
    ans += 1

# Right
target_x = viewpoint_x
for target_y in range(viewpoint_y+1, W, 1):
    if masu[target_x][target_y] == '#':
        break
    ans += 1

print(ans)
