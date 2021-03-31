#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/dp/tasks/dp_b

N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

min_cost = [float('inf')] * N

min_cost[0] = 0

for now_i in range(N):
    for next_i in range( max(now_i+1, 0), min(now_i+K+1, N), 1):
        min_cost[next_i] =  min(min_cost[next_i], min_cost[now_i] + abs(h[now_i]-h[next_i]))

print(min_cost[N-1])
