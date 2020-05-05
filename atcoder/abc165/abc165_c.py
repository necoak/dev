#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc165/tasks/abc165_c

import numpy as np
from itertools import combinations_with_replacement


N, M, Q = map(int, input().split())

abcd_array = []
for i in range(Q):
    abcd = map(int, input().split())
    abcd_array.append(list(abcd))

anslist_candidates = combinations_with_replacement(range(1, M+1), N)

max_anslist_score = 0
for tmp_anslist in anslist_candidates:
    sum_d = 0

    is_valid_anslist = True
    prev_ansitem = tmp_anslist[0]
    for ansitem in tmp_anslist[1:]:
        if prev_ansitem > ansitem:
            is_valid_anslist = False
            break
    if not is_valid_anslist:
        continue

    for ai, bi, ci, di in abcd_array:
        if ((tmp_anslist[bi-1] - tmp_anslist[ai-1]) == ci):
            sum_d += di
    max_anslist_score = max(max_anslist_score, sum_d)

print(max_anslist_score)
