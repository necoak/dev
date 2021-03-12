#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/past202005-open/tasks/past202005_e

n,m,q = list(map(int, input().split()))

uv_graph = {}
for i in range(1, n+1, 1):
    uv_graph[i] =[]
for i in range(1, m+1, 1):
    ui, vi = list(map(int, input().split()))
    uv_graph[ui].append(vi)
    uv_graph[vi].append(ui)

#print(uv_graph)

colors = {}
c_list = list(map(int, input().split()))
for i in range(1, n+1, 1):
    colors[i] = c_list[i-1]
#print(colors)

ans_list = []

for i in range(q):
    #print(colors)

    op, *op_args = list(map(int, input().split()))

    # 
    ans_list.append(colors[op_args[0]])

    if op == 1:
        # スプリンクラー
        target_color = colors[op_args[0]]
        rinsetsu_indexs = uv_graph[op_args[0]]
        for rinsetsu_index in rinsetsu_indexs:
            colors[rinsetsu_index] = target_color
    else:
        # 塗り替え
        colors[op_args[0]] = op_args[1]

for ans in ans_list:
    print(ans)
