#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc075/tasks/abc075_b

h_txt, w_txt = input().split()
h_value = int(h_txt)
w_value = int(w_txt)

banmen = []

def add1_banmen(y,x):
    if y < 0:
        return
    if x < 0:
        return
    if y >= h_value:
        return
    if x >= w_value:
        return
    if banmen[y][x] == '#':
        return
    banmen[y][x] += 1
    return

for y_i in range(h_value):
    gyo_txts = list(input())
    gyo_vals = []
    for x_i in range(w_value):
        if gyo_txts[x_i] == '.':
            gyo_vals.append(0)
        else:
            gyo_vals.append('#')
    banmen.append(gyo_vals)

for y_i in range(h_value):
    for x_i in range(w_value):
        if banmen[y_i][x_i] != '#':
            continue
        add1_banmen(y_i - 1, x_i - 1) # 左上
        add1_banmen(y_i - 1, x_i)     # 上
        add1_banmen(y_i - 1, x_i + 1) # 右上
        add1_banmen(y_i, x_i - 1)     # 左
        add1_banmen(y_i, x_i + 1)     # 右
        add1_banmen(y_i + 1, x_i - 1) #  左下
        add1_banmen(y_i + 1, x_i)     # 下
        add1_banmen(y_i +1, x_i + 1)  # 右下

for y_i in range(h_value):
    for x_i in range(w_value):
        print(banmen[y_i][x_i], end='')
    print()
