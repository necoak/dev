#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc136/tasks/abc136_d

import sys

s = list(input())

child_list = [1 for v in range(len(s))]
child_patterns = []
ans = None

for x in range(10**100):
    
    child_patterns.append([child_list])

    next_child_list = [0 for v in range(len(s))]
    for i,si in enumerate(s):
        if si == 'L':
            next_child_list[i-1] += child_list[i]
        else:
            next_child_list[i+1] += child_list[i]
    
    try:
        izen_no_index = child_patterns.index(next_child_list)
    except ValueError:
        child_list = next_child_list
        continue

    print(child_list)
    if x == izen_no_index:
        ans = child_list
    else:
        ans_pattern_index = ((10**100 - 1 - izen_no_index) % (x - izen_no_index)) +  izen_no_index
        ans = child_patterns[ans_pattern_index]
    break

print(*ans, sep=' ')

