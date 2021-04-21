#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abs/tasks/abc088_b

N = int(input())
a_list = list(map(int, input().split()))

a_list_sorted = sorted(a_list, reverse=True)

alice_sum = 0
bob_sum = 0

for i, ai in enumerate(a_list_sorted):
    if i % 2 == 0:
        alice_sum += ai
    else:
        bob_sum += ai
print(alice_sum-bob_sum)
