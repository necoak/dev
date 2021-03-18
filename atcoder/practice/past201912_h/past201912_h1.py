#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/past201912-open/tasks/past201912_h

n = int(input())
c_list = list(map(int, input().split()))
q = int(input())
s_list =  []

for i in range(q):
    si = list(map(int, input().split()))
    s_list.append(si)

selled_cnt = 0

# ボトルネックとなる最小枚数のカードをカウントアップ
selled_by_tanpin = [0 for _ in range(n)]
selled_by_set = 0
selled_by_all = 0

min_of_set = 10**9
min_of_all = 10**9
for i in range(n):
    if i % 2 == 0:
        min_of_set = min(min_of_set, c_list[i])
    min_of_all =  min(min_of_all, c_list[i])

import math
variation_cnt_of_set = math.ceil(n / 2)
variation_cnt_of_all = n

for i in range(q):
    si = s_list[i]

    # 単品販売
    if si[0]==1:
        x = si[1] - 1 # 販売するcのインデックス
        a = si[2] # 販売する枚数

        # 売れるなら売る
        if x % 2 == 0:
            if c_list[x] - selled_by_set - selled_by_all - selled_by_tanpin[x] >= a:
                selled_by_tanpin[x] += a
                min_of_set = min(min_of_set, c_list[x]-selled_by_tanpin[x])
                min_of_all = min(min_of_all, c_list[x]-selled_by_tanpin[x])
        else:
            if c_list[x] - selled_by_all - selled_by_tanpin[x] >= a:
                selled_by_tanpin[x] += a
                min_of_all = min(min_of_all, c_list[x]-selled_by_tanpin[x])
    
    # セット販売
    if si[0]==2:
        a = si[1] # 販売する枚数
        
        # 奇数番号を売るが売れるか？
        if min_of_set - selled_by_all - selled_by_set >= a:
            selled_by_set += a
    
    # 全種類販売
    if si[0] == 3:
        a = si[1] # 販売する枚数

        # 全番号を売るが売れるか？
        if (min_of_all - selled_by_all >= a) and (min_of_set - selled_by_set - selled_by_all >= a):
            selled_by_all += a

selled_cnt = selled_by_all * variation_cnt_of_all + selled_by_set * variation_cnt_of_set + sum(selled_by_tanpin)
print(selled_cnt)
