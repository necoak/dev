#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc196/tasks/abc196_d

H, W, A, B = list(map(int, input().split()))

banmen = []
for i in range(H):
    banmen.append([False for _ in range(W)])

def dfs_tatami_patterns(now_i, now_j, zan_a, zan_b):
    print('DFS_TATAMI: ', now_i, now_j, zan_a, zan_b)
    if now_j >= W:
        print('pattern-a')
        return dfs_tatami_patterns(now_i+1, 0, zan_a, zan_b)
    if now_i >= H:
        print('X')
        return 1
    
    # すでに配置済みの場合はスキップ
    if banmen[now_i][now_j]:
        print('pattern-b')
        return dfs_tatami_patterns(now_i, now_j+1, zan_a, zan_b)

    ret = 0
    # 半畳を1枚消費して次へ
    banmen[now_i][now_j] = True
    if zan_b >= 1:
        print('pattern-c')
        ret += dfs_tatami_patterns(now_i, now_j+1, zan_a, zan_b-1)
    
    # 1畳を1枚消費して次へ
    if zan_a >= 1:
        # 1畳を横で消費して次へ(まだ横におけるなら)
        if now_j+1 < W:
            print('pattern-d')
            banmen[now_i][now_j+1] = True
            ret += dfs_tatami_patterns(now_i, now_j+1, zan_a-1, zan_b)
            banmen[now_i][now_j+1] = False
        # 1畳を縦で消費して次へ(まだ縦におけるなら) 
        if now_i+1 < H:
            print('pattern-e')
            banmen[now_i+1][now_j] = True
            ret +=  dfs_tatami_patterns(now_i, now_j+1, zan_a-1, zan_b)
            banmen[now_i+1][now_j] = False
    banmen[now_i][now_j] = False
    return ret

print(dfs_tatami_patterns(0, 0, A, B))



