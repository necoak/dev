#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/past202005-open/tasks/past202005_e

MAX_INT = 100000
n,m,q = list(map(int, input().split()))


uv_graph = [[] for _ in range(n)]
for i  in range(m):
    ui, vi = list(map(int, input().split()))
    uv_graph[ui-1].append(vi-1)
    uv_graph[vi-1].append(ui-1)

print(uv_graph)

colors = list(map(int, input().split()))

ans_list = []

for i in range(q):
    print(colors)

    op, *op_args = list(map(int, input().split()))

    # 
    ans_list.append(colors[op_args[0]])

    if op == 1:
        # スプリンクラー
        target_color = colors[op_args[0]-1]
        rinsetsu_indexs = uv_graph[op_args[0]-1]
        for rinsetsu_index in rinsetsu_indexs:
            colors[rinsetsu_index] = target_color
    else:
        # 塗り替え
        colors[op_args[0]-1] = op_args[1]

for ans in ans_list:
    print(ans)
