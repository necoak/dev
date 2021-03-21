#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc196/tasks/abc196_d

H, W, A, B = list(map(int, input().split()))

banmen = []
for i in range(H):
    banmen.append([False for _ in range(W)])

patterns = []

def dfs_tatami_patterns(now_i, now_j, zan_a, zan_b):
    if now_j >= W:
        return dfs_tatami_patterns(now_i+1, 0, zan_a, zan_b)
    if (now_i >= H) and (zan_a == 0) and (zan_b == 0):
        #print(patterns)
        return 1
    
    # すでに配置済みの場合はスキップ
    if banmen[now_i][now_j]:
        return dfs_tatami_patterns(now_i, now_j+1, zan_a, zan_b)

    ret = 0
    # 半畳を1枚消費して次へ
    banmen[now_i][now_j] = True
    if zan_b >= 1:
        patterns.append((now_i, now_j, 'Half'))
        ret += dfs_tatami_patterns(now_i, now_j+1, zan_a, zan_b-1)
        del patterns[-1]
    
    # 1畳を1枚消費して次へ
    if zan_a >= 1:
        # 1畳を横で消費して次へ(まだ横におけるなら＝右端にいない。右隣も空白地。)
        if (now_j+1 < W) and (banmen[now_i][now_j+1] ==False):
            patterns.append((now_i, now_j, '1Joh-L'))
            patterns.append((now_i, now_j+1, '1Joh-R'))

            banmen[now_i][now_j+1] = True
            ret += dfs_tatami_patterns(now_i, now_j+1, zan_a-1, zan_b)
            banmen[now_i][now_j+1] = False

            del patterns[-1]
            del patterns[-1]

        # 1畳を縦で消費して次へ(まだ縦におけるなら＝下端にいない。下隣も空白地。)
        if (now_i+1 < H) and (banmen[now_i+1][now_j] == False):
            patterns.append((now_i, now_j, '1Joh-U'))
            patterns.append((now_i+1, now_j, '1Joh-D'))
            
            banmen[now_i+1][now_j] = True
            ret +=  dfs_tatami_patterns(now_i, now_j+1, zan_a-1, zan_b)
            banmen[now_i+1][now_j] = False

            del patterns[-1]
            del patterns[-1]

    banmen[now_i][now_j] = False
    return ret

print(dfs_tatami_patterns(0, 0, A, B))



