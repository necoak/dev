#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_b

CANT_STR='UNSATISFIABLE'
import sys
from itertools import combinations_with_replacement

a,b,w = list(map(int, input().split()))
w = w*1000

master_gram_pattern = list(range(a, b+1, 1))

if a > w:
    print(CANT_STR)
    sys.exit(0)

max_ko = 0
min_ko = 0

# calc min
def calc_min_kosu(gram):
    gram_max_ko = gram // a
    gram_min_ko = gram // b
    gram_kosu = None
    for kosu in range(gram_min_ko, gram_max_ko+1, 1):
        kumiawase_all = combinations_with_replacement(master_gram_pattern, kosu)
        for kumiawase in kumiawase_all:
            if sum(kumiawase) == w:
                print(kumiawase)
                gram_kosu = kosu
                break
            else:
                continue
        break
    return gram_kosu

# calc min
b_ko = w // b
amari_gram  = w % b
while(b_ko > 0):
    print('b: ', str(b_ko))
    if amari_gram == 0:
        print('SSS')
        min_ko = b_ko
        break
    elif a > amari_gram:
        b_ko -= 1
        amari_gram += b
        continue
    else:
        kosu = calc_min_kosu(amari_gram)
        if kosu is not None:
            min_ko = kosu + b_ko
            break
        else:
            b_ko -= 1
            amari_gram += b
            continue
if min_ko != 0:
    print(min_ko)
else:
    print(CANT_STR)



