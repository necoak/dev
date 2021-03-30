#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/dp/tasks/dp_b
import sys 
from collections import Counter

N, K = list(map(int, input().split()))
h = list(map(int, input().split()))

min_cost = [10**4] * N

min_cost[0] = 0
#min_cost[1] = abs(h[0]-h[1])

for next_i in range(1, N, 1):
    for now_i in range( max(, 0), min(i-1, N), 1):
        min_cost[i] = min(min_cost[i], min_cost[before_i]+abs(h[i]-h[before_i]))

print(min_cost[N-1])
