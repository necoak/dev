#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc126/tasks/abc126_b

intext = input()

head2 = int(intext[0:2])
tail2 = int(intext[2:])

# is_head_yy = False
is_head_mm = False
# is_tail_yy = False
is_tail_mm = False

if 0 < head2 <= 12:
    is_head_mm = True
if 0 < tail2 <= 12:
    is_tail_mm = True

if is_head_mm and is_tail_mm:
    print('AMBIGUOUS')
elif is_head_mm:
    print('MMYY')
elif is_tail_mm:
    print('YYMM')
else:
    print('NA')
