#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc126/tasks/abc126_a

intext1 = input()
[n, k] = map(int, intext1.split())

intext2 = input()

outtext = intext2[:k-1] .lower()
if k == 1:
    outtext = intext2[0].lower() + intext2[1:]
elif k == n:
    outtext = intext2[:k-1] + intext2[k-1].lower()
else:
    outtext = intext2[0:k-1] + intext2[k-1].lower() + intext2[k:]

print(outtext)
