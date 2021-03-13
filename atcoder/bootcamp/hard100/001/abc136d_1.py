#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc136/tasks/abc136_d

s = list(input())

continuous_list = []
continuous_chr = 'R'
continuous_chr_cnt = 0
continuous_chr_s_index = 0
for i,si in enumerate(s):
    if continuous_chr == si:
        # 文字が連続している
        continuous_chr_cnt += 1
        continuous_list.append(None)
        continue
    elif continuous_chr == 'R':
        # 文字が切り替わった R -> L
        # 連続文字情報をRの終点地点(1個前のi)に記録
        continuous_list[i-1] = {'R': continuous_chr_cnt}
        continuous_list.append(None)
        # re-initialize
        continuous_chr = 'L'
        continuous_chr_cnt = 1
        continuous_chr_s_index = i
    else:
        # 文字が切り替わった L -> R
        # 連続文字情報をLのスタート位置に記録
        continuous_list[continuous_chr_s_index] = {'L': continuous_chr_cnt}
        continuous_list.append(None)
        # re-initialize
        continuous_chr = 'R'
        continuous_chr_cnt = 1
        continuous_chr_s_index = i
# end procedure
continuous_list[-1] = {'L': continuous_chr_cnt}

print(continuous_list)

anslist = [0 for v in range(len(s))]
for i,continuous in enumerate(continuous_list):
    if continuous is None:
        continue
    if 'R' in continuous:
        continuous_cnt = continuous['R']
        if continuous_cnt % 2 == 0:
            # even
            continuous_cnt_odd = continuous_cnt // 2 
            continuous_cnt_even = continuous_cnt // 2
        else:
            # odd
            continuous_cnt_odd = continuous_cnt // 2 + 1
            continuous_cnt_even = continuous_cnt // 2
        anslist[i] += continuous_cnt_odd
        anslist[i+1] += continuous_cnt_even
    else:
        continuous_cnt = continuous['L']
        if continuous_cnt % 2 == 0:
            # even
            continuous_cnt_odd = continuous_cnt // 2
            continuous_cnt_even = continuous_cnt // 2
        else:
            # odd
            continuous_cnt_odd = continuous_cnt // 2 + 1
            continuous_cnt_even = continuous_cnt // 2
        anslist[i] += continuous_cnt_odd
        anslist[i-1] += continuous_cnt_even

print(*anslist, sep=' ')

