#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_d

import copy
n, m, q = list(map(int, input().split()))

wv_list = []
for i in range(n):
    wi, vi = list(map(int, input().split()))
    wv_list.append((wi, vi))

x_list = list(map(int, input().split()))

query_list = []
for i in range(q):
    l, r = list(map(int, input().split()))
    query_list.append((l,r))

def calc_donyoku(my_x, my_wv_list):
    max_index = -1
    max_v = -1
    for i, (my_wi, my_vi) in enumerate(my_wv_list):
        if ((my_wi <= my_x) and (my_vi > max_v)):
            max_v = my_vi
            max_index = i
    return max_index, max_v
            
for li,ri in query_list:
    # print('-----')
    x_list_half1 = x_list[0:li-1]
    x_list_half2 = x_list[ri:]
    # print(x_list_half1, x_list_half2)
    x_list_for_solve = sorted(x_list_half1 + x_list_half2)
    # print(x_list_for_solve)
    wv_list_for_solve = copy.deepcopy(wv_list)
    ans = 0
    for xi in x_list_for_solve:
        donyoku_i, donyoku_v = calc_donyoku(xi, wv_list_for_solve)
        if donyoku_i != -1:
            wv_list_for_solve.pop(donyoku_i)
            ans += donyoku_v
    print(ans)


