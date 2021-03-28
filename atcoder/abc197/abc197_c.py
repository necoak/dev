#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc196/tasks/abc196_c
import sys
from functools import reduce

sys.setrecursionlimit(20000)

N = int(input())
A = list(map(int, input().split()))

ans = 2**30

def orxor(nums_list):
    #print('orxor:',nums_list)
    or_vals = []
    for nums in nums_list:
        if len(nums) >= 2:
            or_vals.append(reduce(lambda x, y: x | y, nums))
        else:
            or_vals.append(nums[0])
    if len(or_vals) >= 2:
        xor_val = reduce(lambda x,y: x^y, or_vals)
    else:
        xor_val = or_vals[0]
    return xor_val

def calc_or(nums):
    if len(nums) >= 2:
        return reduce(lambda x, y: x | y, nums)
    else:
        return nums[0]

def calc_xor(nums):
    if len(nums) >= 2:
        return reduce(lambda x,y: x^y, nums)
    else:
        return nums[0]

def dfs(xor_val, unfixed_nums):
    global ans

    if len(unfixed_nums) == 0:
        ans = min(ans, xor_val)
        if ans==0:
            print(0)
            sys.exit(0)
    
    for i in range(1, len(unfixed_nums)+1):
        this_fixed_nums = unfixed_nums[:i]
        next_unfixed_nums = unfixed_nums[i:]
        
        this_or_val = calc_or(this_fixed_nums)
        if xor_val is None:
            this_xor_val = this_or_val
        else:
            this_xor_val = calc_xor([xor_val, this_or_val])
        dfs(this_xor_val, next_unfixed_nums)


dfs(None, A)
print(ans)