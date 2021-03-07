#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc191/tasks/abc191_b

n = int(input())

a_list = []
b_list = []
ab_list = []
for i in range(n):
    ai, bi = list(map(int, input().split()))
    a_list.append(ai)
    b_list.append(bi)
    ab_list.append(ai+bi)

a_min = min(a_list)


# パターン1 .. A min -> B min
ans1 = 0
min_a = 0
min_b = 0

min_a = min(a_list)
min_a_indx = a_list.index(min_a)

# 複数人の場合？
if a_list.count(min_a) > 1:
    min_b = min(b_list)
else:
    tmp = b_list.pop(min_a_indx)
    min_b = min(b_list)
    b_list.insert(min_a_indx, tmp)

ans1 = max(min_a, min_b)


# パターン2 .. B min -> A min
ans2 = 0
min_b = min(b_list)
ans2 += min_b
min_b_indx = b_list.index(min_b)

# 複数人の場合？
if b_list.count(min_b) > 1:
    min_a = min(a_list)
else:
    tmp = a_list.pop(min_b_indx)
    min_a = min(a_list)
    a_list.insert(min_a_indx, tmp)
ans2 = max(min_a, min_b)

# パターン3 .. AB min
ans3 = min(ab_list)

ans = min([ans1, ans2, ans3])
print(ans)
