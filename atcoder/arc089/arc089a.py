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
    jouken1 = (now_next_timewidth >= now_next_distance)
    jouken2 = ((now_next_timewidth - now_next_distance) % 2 == 0)
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

def calc_next_kanousei(kanousei_set, now_t, next_t, next_x, next_y):
    next_kanousei_set = set()
    for kanousei_x, kanousei_y in kanousei_set:
        if kanousei_x - 1 >= 0 and can_go(now_t, kanousei_x-1, kanousei_y, next_t, next_x, next_y):
            next_kanousei_set.add((kanousei_x-1, kanousei_y))
        if kanousei_x + 1 <= MAX_X and can_go(now_t, kanousei_x+1, kanousei_y, next_t, next_x, next_y):
            next_kanousei_set.add((kanousei_x+1, kanousei_y))
        if kanousei_y - 1 >= 0 and can_go(now_t, kanousei_x, kanousei_y-1, next_t, next_x, next_y):
            next_kanousei_set.add((kanousei_x, kanousei_y-1))
        if kanousei_y + 1 <= MAX_Y and can_go(now_t, kanousei_x, kanousei_y+1, next_t, next_x, next_y):
            next_kanousei_set.add((kanousei_x, kanousei_y+1))
    return next_kanousei_set

check(txy_list)

kanousei_set = set([(0,0)])
now_t = 0
for i in range(N):
    next_target_t, next_target_x, next_target_y = txy_list[i]
    # 目的タイムまでを探索
    for now_t in range(now_t+1, next_target_t+1):
        kanousei_set = calc_next_kanousei(kanousei_set, now_t, next_target_t, next_target_x, next_target_y)
    # 目的タイムでの現在地にいるか
    if (next_target_x, next_target_y) not in kanousei_set:
        print('No')
        sys.exit(0)
    # 中間ポイントを可能性の原点の置き直す
    kanousei_set = set([(next_target_x, next_target_y)])
    # print('[Check]', now_t, kanousei_set)

print('Yes')
