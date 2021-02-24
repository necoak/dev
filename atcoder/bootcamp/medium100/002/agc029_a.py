#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/agc029/tasks/agc029_a

s_txt = list(input())
n = len(s_txt)
cnt = 0

while(True):
    for indx in range(n-1, 0, -1):
        if ((s_txt[indx] == 'W') and (s_txt[indx-1] == 'B')):
            s_txt[indx] = 'B'
            s_txt[indx-1] = 'W'
            cnt += 1
            break
        
        if indx == 1:
            print(cnt)
            exit(0)
