#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_a
from itertools import combinations
from collections import Counter

n = int(input())
a_list  = list(map(int, input().split()))

a_counter = Counter(a_list)

a_patterns = combinations(range(-200, 200+1,1),2)

ans = 0
for ai, aj in a_patterns:
    ai_cnt = a_counter[ai]
    aj_cnt = a_counter[aj]
    ans += ai_cnt * aj_cnt * (ai-aj)**2

print(ans)
