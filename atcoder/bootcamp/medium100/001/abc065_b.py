#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc065/tasks/abc065_b

n = int(input())
an = {}
for i in range(1,n+1):
    an[i] = int(input())

#print(an)

next_indx = 1
#rireki =  []
cnt = 0

while(True):
    #print("++++" + str(next_indx))
    if next_indx == 2:
        print(cnt)
        exit(0)

    tmp_next_indx = an[next_indx]

    if cnt > n:
        print("-1")
        exit(0)
#    rireki.append(tmp_next_indx)
    next_indx = tmp_next_indx
    cnt += 1



