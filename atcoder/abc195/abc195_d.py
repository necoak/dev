#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_d

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

# create graph
box_baggage_graph = []
for xi in x_list:
    tmp_list = []
    for j, wj,vj in enumerate(wv_list):
        if xi >= wj:
            tmp_list.append(j)

# solve query
for li, ri in query_list:
    # graph update
    query_i_box_baggage_graph = box_baggage_graph[0:li] + box_baggage_graph[ri:]

    for box_baggage in query_i_box_baggage_graph:
        for baggage in box_baggage:
            


