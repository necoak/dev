#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc145/tasks/abc145_c

n_text = input()
n = int(n_text)

class Zahyo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @staticmethod
    def parse(text):
        x_txt, y_txt = text.split()
        x = int(x_txt)
        y = int(y_txt)
        zahyo = Zahyo(x, y)
        return zahyo


def calc_kyori(zahyo1, zahyo2):
    kyori = (((zahyo1.x - zahyo2.x) ** 2) + ((zahyo1.y - zahyo2.y) ** 2)) ** 0.5
    return kyori


def calc_kyoris(my_zahyo_list):
    kyori = 0
    for i in range(len(my_zahyo_list)-1):
        kyori += calc_kyori(my_zahyo_list[i], my_zahyo_list[i+1])
    return kyori


zahyo_list = []
for i in range(n):
    zahyo_list.append(Zahyo.parse(input()))

kyori_list = []


def calc(my_kakutei_zahyo_list, my_un_kakutei_zahyo_list, my_kyori_list):
    # print(len(my_kakutei_zahyo_list), len(my_un_kakutei_zahyo_list))
    if len(my_un_kakutei_zahyo_list) == 0:
        kyori = calc_kyoris(my_kakutei_zahyo_list)
        my_kyori_list.append(kyori)
    for i in range(len(my_un_kakutei_zahyo_list)):
        calc(my_kakutei_zahyo_list + [my_un_kakutei_zahyo_list[i]], my_un_kakutei_zahyo_list[0:i] + my_un_kakutei_zahyo_list[i+1:], my_kyori_list)


calc([], zahyo_list, kyori_list)

heikin = sum(kyori_list) / len(kyori_list)
print(heikin)
