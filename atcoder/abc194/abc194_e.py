#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc194/tasks/abc194_e

def calc_mex(fullset, subset):
    return min(fullset - subset)

n, m = list(map(int, input().split()))
a_list = list(map(int, input().split()))

bosyugo = set(range(n))

ans = max(bosyugo) + 1

# m個のサイズの部分リスト生成を i=0からn-mまで
for i in range(n-m):
    sub_a_set = set(a_list[i:i+m])
    tmp_ans = calc_mex(bosyugo, sub_a_set)
    if tmp_ans < ans:
        ans = tmp_ans
        if ans == 0:
            break

print(ans)
