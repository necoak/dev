#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/agc040/tasks/agc040_a

MAX_INT = 100000
s_txt = input()

MIN_V = 1000000

def func(my_suretu, my_s_txt, min_v):
    #print('func(', my_suretu, my_s_txt, min_v, ')')

    now_sum = sum(my_suretu)
    # print(now_sum)
    if (now_sum >= min_v):
        return min_v

    if (len(my_s_txt) == 0):
        if (now_sum < min_v):
            min_v = now_sum
        return min_v
    else:
        next_my_s_txt = my_s_txt[1:]

    for v in range(0, MAX_INT):
        new_min_v = min_v
        if (len(my_suretu)==0):
            new_min_v = func(my_suretu + [v], next_my_s_txt, min_v)
        elif (((my_s_txt[0] == '>') and (my_suretu[-1] > v)) or 
            ((my_s_txt[0] == '<') and (my_suretu[-1] < v))):
            #print(my_suretu[-1], my_s_txt[0], v)
            new_min_v = func(my_suretu + [v], next_my_s_txt, min_v)
        if (new_min_v < min_v):
            min_v = new_min_v
        elif ((new_min_v == min_v) and (new_min_v != MIN_V)):
            break

    return min_v
        
min_v = MIN_V
for v in range(0, MAX_INT):
    new_min_v = func([v], s_txt, min_v)
    if (new_min_v < min_v):
        min_v = new_min_v
    elif ((new_min_v == min_v) and (new_min_v != MIN_V)):
        break

print(min_v)

