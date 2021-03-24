#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc114/tasks/abc114_c

N = int(input())

ans = 0

def dfs(base_val, used3, used5, used7):
    global ans
    if base_val > N:
        return

    if (used3 and used5 and used7):
        ans += 1
    
    dfs(base_val * 10 + 3, True, used5, used7)
    dfs(base_val * 10 + 5, used3, True, used7)
    dfs(base_val * 10 + 7, used3, used5, True)

dfs(0, False, False, False)
print(ans)
