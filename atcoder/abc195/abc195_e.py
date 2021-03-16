#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc195/tasks/abc195_e

n = int(input())
s = input()
x = input()

# init 
patterns = [s[0],'0']
# 1~
for i in range(1,n):
    new_patterns = []
    for pattern in patterns:
        new_patterns.append(pattern+s[i])
        new_patterns.append(pattern+'0')
    patterns = new_patterns

can_div7_list = []
for pattern in patterns:
    if (int(pattern) % 7 == 0):
        can_div7_list.append(True)
    else:
        can_div7_list.append(False)

pcdl = zip(patterns, can_div7_list)

keika = ''

def calc_score(s_start_str):
    candiv7_list = \
        [pat for pat, candiv7 in pcdl \
            if pat.startswith(s_start_str) and candiv7]
    return len(candiv7_list)


for i, xi in enumerate(x):
    next_keika0 = keika + '0'
    next_keika1 = keika + s[i]

    next_keika0_score = calc_score(next_keika0)
    next_keika1_score = calc_score(next_keika1)
    if xi == 'A' and next_keika0_score > next_keika1_score:
        # Mr.A selects lower scored one.
        keika = next_keika1
    elif xi == 'A' and next_keika0_score < next_keika1_score:
        # Mr.A selects lower scored one.
        keika = next_keika0
    elif xi == 'T' and  next_keika0_score > next_keika1_score:
        # Mr.K selects bigger scored one.
        keika = next_keika0
    else:
        keika = next_keika1

if(int(keika) % 7 == 0):
    print('Takahashi')
else:
    print('Aoki')

