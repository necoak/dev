#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/agc033/tasks/agc033_a
import numpy as np

h, w = map(int, input().split())
inputs = []
for i in range(h):
    input_text_i = input()
    input_text_i.replace('.', 0)
    input_text_i.replace('#', 1)
    input_i = [int(v) for v in input_text_i]
    for j in range(w):
        inputs[i][j] = input_i[j]

for i in range(h):
    for j in range(w):
        