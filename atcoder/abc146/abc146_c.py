#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc146/tasks/abc146_c

a_txt, b_txt, x_txt = input().split()
a = int(a_txt)
b = int(b_txt)
x = int(x_txt)

def calc_need_money(seisu):
    seisu_txt = str(seisu)
    return ((a * seisu) + (b * (len(seisu_txt))))

def can_buy(seisu, my_money):
    need_money = calc_need_money(seisu)
    #print(str(seisu) + ' need_money:need_money:' + str(need_money))
    #print(str(my_money))
    return my_money >= need_money


for v in range(1, 1000000000 + 10000 + 1, 10000):
    # print(v)
    if can_buy(v, x):
        #print('can_buy')
        continue
    elif v == 1:
        #print('RouteA')
        print(0)
        exit()
    elif v == 10000:
        #print('RouteB')
        for v2 in range(1, 10001):
            print(v2)
            if can_buy(v2, x):
                continue
            else:
                print(v2 - 1)
                exit()
    else:
        #print('routeC')
        for v2 in range(v-10000, v+1):
            #print(v2)
            if can_buy(v2, x):
                continue
            else:
                print(v2 - 1)
                exit()
print('1000000000')
