#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc165/tasks/abc182_a

import sys
import math
from functools import reduce

def mygcd(*numbers):
    return reduce(math.gcd, numbers)

input_n = input()
input_alist = input()

n = int(input_n)
alist_s = input_alist.split()


alist = [int(x) for x in alist_s]

# ans = mygcd(*alist)

def calc_gcd_do(numbers):
    # print(numbers)
    ans = mygcd(*numbers)
    if ans != 1:
        print(ans)
        sys.exit(0)
    # １個減らす
    #   print(numbers)
    for i in range(len(numbers)):
        new_numbers = []
        if i==0:
            new_numbers = numbers[1:]
        elif i==len(numbers):
            new_numbers = numbers[:-1]
        else:
            new_numbers = numbers[0:i] + numbers[i+1:]
        print(new_numbers)
        ans = mygcd(*new_numbers)
        print(ans)
        if ans != 1:
            print(ans)
            sys.exit(0)

calc_gcd_do(alist)

# print(ans)
