#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc007/tasks/abc007_3

R,C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
c = []
for gyo in range(R):
    c_gyo = list(input())
    c.append(c_gyo)

from collections import deque

visited = []
for _ in range(R):
    visited.append([False for _ in range(C)])

next_queue = deque()
next_queue.append((sy-1,sx-1,0))

ans = -1
while len(next_queue) >= 0:
    #print(next_queue)

    current_y, current_x, current_turn_num  = next_queue.popleft()

    if ((current_y == gy-1) and (current_x == gx-1)):
        ans = current_turn_num
        break

    # go left
    next_y = current_y
    next_x = current_x - 1
    next_turn_num = current_turn_num + 1
    if ((next_x >= 0) and (c[next_y][next_x] == '.') and (visited[next_y][next_x] == False)):
        visited[next_y][next_x] = True
        next_queue.append((next_y, next_x, next_turn_num))

    # go right
    next_y = current_y
    next_x = current_x + 1
    next_turn_num = current_turn_num + 1
    if ((next_x < C) and (c[next_y][next_x] == '.') and (visited[next_y][next_x] == False)):
        visited[next_y][next_x] = True
        next_queue.append((next_y, next_x, next_turn_num))

    # go up
    next_y = current_y - 1
    next_x = current_x
    next_turn_num = current_turn_num + 1
    if ((next_y >= 0) and (c[next_y][next_x] == '.') and (visited[next_y][next_x] == False)):
        visited[next_y][next_x] = True
        next_queue.append((next_y, next_x, next_turn_num))

    # go down
    next_y = current_y + 1
    next_x = current_x
    next_turn_num = current_turn_num + 1
    if ((next_y < R) and (c[next_y][next_x] == '.') and (visited[next_y][next_x] == False)):
        visited[next_y][next_x] = True
        next_queue.append((next_y, next_x, next_turn_num))

print(ans)