#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/typical90/tasks/typical90_d

import sys
sys.setrecursionlimit(10**5)

H, W = list(map(int, input().split()))

A = []
for i in range(H):
    A.append(list(map(int, input().split())))

a_gyo_sum_list = []
for i in range(H):
    a_gyo_sum_list.append(sum(A[i]))

a_retu_sum_list = []
for j in range(W):
    retu_sum = 0
    for i in range(H):
        retu_sum += A[i][j]
    a_retu_sum_list.append(retu_sum)

for i in range(H):
    gyo_print_strs = []
    for j in range(W):
        gyo_print_strs.append(str(a_gyo_sum_list[i] + a_retu_sum_list[j] - A[i][j]))
    print(' '.join(gyo_print_strs))
