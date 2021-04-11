#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc086/tasks/arc089_a


import sys

N =  int(input())
MAX_X = 10**5
MAX_Y = 10**5

txy_list = []
for _ in range(N):
    txy_list.append(list(map(int, input().split())))

def can_go(now_t, now_x, now_y, next_t,  next_x, next_y):
    now_next_distance = abs(now_x - next_x) + abs(now_y - next_y)
    now_next_timewidth = next_t - now_t
    jouken1 = now_next_timewidth >= now_next_distance
    jouken2 = (now_next_timewidth - now_next_distance) % 2 == 0
    return jouken1 and jouken2

# 絶対に行き着かない中間地点同士はないか
def check(txy_list):
    now_t, now_x, now_y = 0, 0, 0
    for i in range(N):
        next_target_t, next_target_x, next_target_y = txy_list[i]
        if not can_go(now_t, now_x, now_y, next_target_t, next_target_x, next_target_y):
            print('No')
            sys.exit(0)
        now_t = next_target_t
        now_x = next_target_x
        now_y = next_target_y

check(txy_list)
print('Yes')
