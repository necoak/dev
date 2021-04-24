#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/typical90/tasks/typical90_b

import sys
sys.setrecursionlimit(10**5)

N = int(input())

def dp(fixed_str, stacked_kakko_cnt):
    #print(fixed_str)
    if len(fixed_str)==N:
        if stacked_kakko_cnt == 0:
            print(fixed_str)
        return
    
    
    next_fixed_str1 = fixed_str+"("
    next_stacked_kakko_cnt1 = stacked_kakko_cnt+1
    dp(next_fixed_str1, next_stacked_kakko_cnt1)

    next_fixed_str2 = fixed_str+")"
    next_stacked_kakko_cnt2 = stacked_kakko_cnt-1
    if next_stacked_kakko_cnt2 >= 0:
        dp(next_fixed_str2, next_stacked_kakko_cnt2)

dp("", 0)
