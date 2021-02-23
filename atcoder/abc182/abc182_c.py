#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc165/tasks/abc182_c

import sys

n_str = input()
n_list = {}

def make_n_list(n_list_x, deleted_keta):
    #print("make_n_list", n_list_x, deleted_keta)

    if deleted_keta in n_list:
        n_list[deleted_keta].append(int(n_list_x))
    else:
        n_list[deleted_keta] = [int(n_list_x)]

    if len(n_list_x) == 1:
        return
    for i in range(len(n_list_x)):
        next_n_lixt_x = []
        if i == 0:
            next_n_lixt_x = n_list_x[1:]
        elif i == len(n_list_x):
            next_n_lixt_x = n_list_x[:-1]
        else:
            next_n_lixt_x = n_list_x[0:i] + n_list_x[i+1:]
        make_n_list(next_n_lixt_x, deleted_keta+1)

make_n_list(n_str,0)

for i in range(len(n_str)):
    n_list_x = n_list[i]
    for val in n_list_x:
        if val % 3 == 0:
            print(i)
            sys.exit(0)
print(-1)

