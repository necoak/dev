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

for i in range(q):
    si = s_list[i]

    # 単品販売
    if si[0]==1:
        x = si[1] - 1 # 販売するcのインデックス
        a = si[2] # 販売する枚数

        # 売れるなら売る
        if c_list[x] >= a:
            c_list[x] -= a
            selled_cnt += a
    
    # セット販売
    if si[0]==2:
        a = si[1] # 販売する枚数
        
        # 奇数番号を売るが売れるか？
        can_sell = True
        for j in range(0, n, 2):
            if c_list[j] < a:
                can_sell = False
                break
        
        if can_sell:
            for j in range(0, n, 2):
                c_list[j] -= a
                selled_cnt += a
    
    # 全種類販売
    if si[0] == 3:
        a = si[1] # 販売する枚数

        # 全番号を売るが売れるか？
        can_sell = True
        for j in range(0, n, 1):
            if c_list[j] < a:
                can_sell = False
                break
        
        if can_sell:
            for j in range(0, n, 1):
                c_list[j] -= a
                selled_cnt += a
    
    # print(c_list, selled_cnt)

print(selled_cnt)
