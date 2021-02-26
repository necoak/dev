#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc066/tasks/abc066_b

s_txt = input()

while(True):
    s_txt = s_txt[0:-1]
    s_txt_len = len(s_txt)
    s_txt_len_half = s_txt_len // 2

    if (s_txt_len % 2) == 1:
        continue

    zenhan = s_txt[0:s_txt_len_half]
    kouhan = s_txt[s_txt_len_half:]
    if zenhan == kouhan:
        print(s_txt_len)
        break
