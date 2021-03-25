#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
h = list(map(int, input().split()))

min_cost = [10**4] * N

min_cost[0] = 0
min_cost[1] = abs(h[0]-h[1])

for i in range(2, N, 1):
    min_cost[i] = min(
        min_cost[i-1]+abs(h[i]-h[i-1]),
        min_cost[i-2]+abs(h[i]-h[i-2]),
    )

print(min_cost[N-1])

