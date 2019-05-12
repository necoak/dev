#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_a
import itertools

intext = input()
[n, k] = map(int, intext.split())

int_list = [v for v in range(1, n+1)]
nk_combis = itertools.combinations(int_list, k)
ans_nk_combis_cnt = 0

for nk_combi in nk_combis:
    # nk_list = list(nk_combi)

    prev_item = None
    is_renzoku = True

    for nk_item in nk_combi:
        if (prev_item != None) and (prev_item + 1 != nk_item):
            is_renzoku = False
            break
        prev_item = nk_item

    if is_renzoku:
        ans_nk_combis_cnt += 1

print(ans_nk_combis_cnt)

