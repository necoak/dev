#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/past202005-open/tasks/past202005_h


N, L = list(map(int, input().split()))
x = set(map(int, input().split()))
T1, T2, T3 = list(map(int, input().split()))

def calc_cost_by_action1(s_index):
    cost = 0
    # run 1
    cost += T1
    # add hardle
    if s_index+1 in x:
        cost += T3
    return cost

def calc_cost_by_action2(s_index):
    cost = 0
    # run 0.5 & 0.5
    cost += T1
    # jump 1
    cost += T2
    # add hardle
    if s_index+2 in x:
        cost += T3
    return cost

def calc_cost_by_action3(s_index):
    cost = 0
    # run 0.5 &  0.5
    cost += T1
    # jump3
    cost += (T2*3)
    # add hardle
    if s_index+4 in x:
        cost += T3
    return cost

min_cost = [0] * (L+1)

min_cost[0] = 0

for i in range(1, L+1, 1):
    # calc goto-i's min cost
    ## by action1
    min_cost[i] = min_cost[i-1] + calc_cost_by_action1(i-1)
    if i-2 >= 0:
        min_cost[i] = min(min_cost[i], min_cost[i-2] + calc_cost_by_action2(i-2))
    if i-4 >= 0:
        min_cost[i] = min(min_cost[i], min_cost[i-4] + calc_cost_by_action3(i-4))
    #print('pos[%s] : %s' % (i, min_cost[i]))

# last jump patttern(action2)
if L-1 >= 0:
    min_cost[L] = min(min_cost[L], min_cost[L-1] + (T1 / 2) + (T2 / 2) )

# last jump pattern (action3) -2
if L-2 >= 0:
    min_cost[L] = min(min_cost[L], min_cost[L-2] + (T1 / 2) + T2 + (T2 / 2) )

# last jump pattern (action3) -3
if L-3 >= 0:
    min_cost[L] = min(min_cost[L], min_cost[L-3] + (T1 / 2) + (T2 * 2) + (T2 / 2) )

print(min_cost[L])
