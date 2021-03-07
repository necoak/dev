#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc194/tasks/abc194_e

import sys

def calc_mex(fullset, subset):
    return min(fullset - subset)

n, m = list(map(int, input().split()))
a_list = list(map(int, input().split()))

# 値(0,1,..)が出現する区間の長さを計算していって、M以下のものを探す
for val in range(n+1):
    x_pos_list = [i for i,x in enumerate(a_list) if x==val]

    if len(x_pos_list)==0:
        print(val)
        sys.exit(0)

    if len(x_pos_list)==1:
        if ((x_pos_list[0] >= m) or (x_pos_list[0] < m+n)):
            print(val)
            sys.exit(0)

    for x_pos_index in range(0, len(x_pos_list)-1, 1):
        sa = x_pos_list[x_pos_index+1] - x_pos_list[x_pos_index]
        print(val, x_pos_list[x_pos_index+1], x_pos_list[x_pos_index], sa)
        if sa >= m:
            print(val)
            sys.exit(0)
