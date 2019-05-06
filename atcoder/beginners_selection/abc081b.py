#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc081_b

n = int(input())
intext = input()
innums = map(int, intext.split())
ni_no_baisu_s = []
for innum in innums:
    nino_baisu = 0
    while True:
        amari = innum % 2
        if amari != 0:
            break
        else:
            innum = innum / 2
            nino_baisu += 1
    ni_no_baisu_s.append(nino_baisu)
min_ni_no_basu = min(ni_no_baisu_s)
print(min_ni_no_basu)
