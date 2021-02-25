#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/agc029/tasks/agc029_a

s_txt = input()
n = len(s_txt)
cnt = 0

while(True):

        s_txt_reverse = s_txt[::-1]
        try:
            indx = s_txt_reverse.index('WB')
        except ValueError:
            print(cnt)
            exit(0)

        s_txt_reverse_replace = s_txt_reverse[0:indx] + 'BW' + s_txt_reverse[indx+2:]
        s_txt = s_txt_reverse_replace[::-1]
        cnt += 1

