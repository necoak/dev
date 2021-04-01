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

    next_yx_list = [
        (current_y-1, current_x),
        (current_y+1, current_x),
        (current_y, current_x-1),
        (current_y, current_x+1)]
    
    for next_y, next_x in next_yx_list:
        if ((0 <= next_y < R) and (0 <= next_x < C) and 
            (c[next_y][next_x] == '.') and (visited[next_y][next_x] == False)):
            visited[next_y][next_x] = True
            next_queue.append((next_y, next_x, current_turn_num+1))

print(ans)