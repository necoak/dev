#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc145/tasks/abc145_b

n_text = input()
n = int(n_text)

s_text = input()

if n % 2 != 0:
    print('No')
    exit()

half_n = int(n / 2)
half_b_text = s_text[0:half_n]
half_a_text = s_text[half_n:n]

# print(half_b_text)
# print(half_a_text)
if half_b_text == half_a_text:
    print('Yes')
else:
    print('No')