#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/dp/tasks/dp_b

N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

min_cost = [10**4] * N

min_cost[0] = 0
min_cost[1] = abs(h[0]-h[1])

for i in range(2, N, 1):
    
    for j in range(i-1, i-K-1, -1):
        if 0 <= j < N:
            min_cost[i] = min(min_cost[i], min_cost[j]+abs(h[i]-h[j]))

print(min_cost[N-1])
