#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b


import sys

S =  input()

KEYENCE_STRING = 'keyence'

keyence_str_index = 0
remove_len = len(S) - len(KEYENCE_STRING)
for remove_start_index in range(0, len(S)-remove_len, 1):
    removed_s = None
    if remove_start_index == 0:
        removed_s = S[remove_len:]
    else:
        removed_s = S[0:remove_start_index] + S[remove_start_index+remove_len:]
    #print(remove_start_index, removed_s)
    if removed_s == KEYENCE_STRING:
        print('YES')
        sys.exit(0)
print('NO')
