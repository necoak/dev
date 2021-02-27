#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc139/tasks/abc139_d
from functools import reduce
from itertools import permutations

n_value = int(input())

i_list = [x for x in range(1,n_value+1)]
# print(i_list)

p_lists = permutations(i_list)
#print(p_lists)

def mod(x,y):
    return x % y

def sum(l):
    return reduce(lambda x,y: x+y, l)

def modsum(p_list):
    return sum(map(mod, i_list, p_list))

print(max(map(modsum, p_lists)))