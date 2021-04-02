#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc072/tasks/arc082_a

N = int(input())
a_list = list(map(int, input().split()))

a_plus1_list = list(map(lambda x:x+1, a_list))
a_minus1_list = list(map(lambda x:x-1, a_list))

a_series_list = sorted(list(set(a_list+a_plus1_list+a_minus1_list)))

# aiまで選択したバリエーションを入れる箱
pattern = []
for i in range(N+1):
    pattern.append([0]*len(a_series_list))

for i in range(1,N+1):
    a_plmi_0_series_index = a_series_list.index(a_list[i-1])
    a_plus_1_series_index = a_series_list.index(a_list[i-1]+1)
    a_minus_1_series_index = a_series_list.index(a_list[i-1]-1)

    for j in range(len(pattern[i])):
        pattern[i][j] = pattern[i-1][j]
    
    pattern[i][a_plmi_0_series_index] += 1
    pattern[i][a_plus_1_series_index] += 1
    pattern[i][a_minus_1_series_index] += 1

print(max(pattern[N]))
