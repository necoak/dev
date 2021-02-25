#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/agc029/tasks/agc029_a

s_txt = list(input())
len_s = len(s_txt)

num_of_b = 0
start_score = 0
for indx, s_txt_i in enumerate(s_txt):
    if s_txt_i == 'B':
        start_score += indx
        num_of_b += 1

end_score = 0
for indx in range(len_s - num_of_b, len_s, 1):
    end_score += indx

print(end_score - start_score)