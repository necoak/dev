#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc064/tasks/abc064_c

from collections import Counter

def calc_rate(score):
    if score <=399:
        return 'gray'
    elif score <= 799:
        return 'brown'
    elif score <= 1199:
        return 'green'
    elif score <= 1599:
        return 'water'
    elif score <= 1999:
        return 'blue'
    elif score <= 2399:
        return 'yellow'
    elif score <= 2799:
        return 'orange'
    elif score <= 3199:
        return 'red'
    else:
        return 'any'

n = int(input())
a_list = list(map(int, input().split()))

a_rates = list(map(calc_rate, a_list))

a_rate_count = Counter(a_rates)

#print(a_rate_count)

min_val = 0
max_val = 0
if a_rate_count['any'] == n:
    min_val = 1
    max_val = n
elif 'any' in a_rate_count:
    min_val = len(a_rate_count)-1
    max_val = min_val + a_rate_count['any']
else:
    min_val = len(a_rate_count)
    max_val = min_val


print(min_val, max_val)
