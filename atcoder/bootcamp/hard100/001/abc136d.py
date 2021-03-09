#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc136/tasks/abc136_d

s = list(input())

child_list = [1 for v in range(len(s))]

for x in range(10**100):
    next_child_list = [0 for v in range(len(s))]
    for i,si in enumerate(s):
        if si == 'L':
            next_child_list[i-1] += child_list[i]
        else:
            next_child_list[i+1] += child_list[i]
    child_list = next_child_list

print(child_list)

