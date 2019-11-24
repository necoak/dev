#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc146/tasks/abc146_b

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

n_txt = input()
n = int(n_txt)

s_txt = input()


for s_chr in s_txt:
    pos = alphabets.find(s_chr)
    print(alphabets[pos + n], end='')
print()
