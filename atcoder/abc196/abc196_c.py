#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc196/tasks/abc196_c

import math
import sys

n_str = input()
n = int(n_str)

n_no_keta = math.floor(math.log10(n)) + 1
ans = 0

# 最終桁１つ手前まで
for i_keta in range(1, n_no_keta-1, 2):
    if i_keta == 1:
        up = 9
    else:
        half_keta = int(i_keta // 2)
        up =  10**(half_keta+1) - 10**half_keta
    #print('iketa', i_keta, up)
    ans += up


# 最終桁の計算
## 最終桁は偶数ではないときはfin
if n_no_keta % 2 != 0:
    print(ans)
    sys.exit(0)

## 最終桁も偶数のときはnのところまで数え上げる
half_n_str = n_str[0:n_no_keta//2]
half_n = int(half_n_str)

ans += (half_n - 10**((n_no_keta//2)-1))

if n >= (half_n + half_n * (10**(n_no_keta//2))):
    ans += 1

print(ans)

