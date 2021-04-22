#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/arc065_a
import re

S = input()
match_obj = re.fullmatch('(dream|dreamer|erase|eraser)+', S)
if match_obj is not None:
    print('YES')
else:
    print('NO')
