#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc088/tasks/abc088_b

n = int(input())
a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

alice_score = 0
bob_score = 0

for i in range(n):
    if ((i % 2) == 0):
        alice_score += a_list[i]
    else:
        bob_score += a_list[i]

print(alice_score-bob_score)