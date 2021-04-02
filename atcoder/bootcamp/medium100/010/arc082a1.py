#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc072/tasks/arc082_a

N = int(input())
a_list = list(map(int, input().split()))

aval_and_apopears_dict = {}

for i in range(N):
    
    for ai_val in [a_list[i], a_list[i]-1, a_list[i]+1]:

        if ai_val in aval_and_apopears_dict:
            aval_and_apopears_dict[ai_val] += 1
        else:
            aval_and_apopears_dict[ai_val] = 1

max_appears = 0
for aval in list(aval_and_apopears_dict):
    max_appears = max(max_appears, aval_and_apopears_dict[aval])

print(max_appears)
