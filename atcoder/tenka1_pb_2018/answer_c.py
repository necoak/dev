
"""
### 問題文
* 整数が N 個与えられます。i 個目の整数は Ai です。 これらを好きな順に一列に並べるとき、隣り合う要素の差の合計の最大値を求めてください。

* 制約
  * `2≤N≤105`
  * `1≤Ai≤109`
  * 入力はすべて整数である

### 入力
* 入力は以下の形式で標準入力から与えられる。
```
N
A1
:
AN
```
"""

def calc_tonari_sa_total(a_list):
    total = 0
    for i in range(1, len(a_list), 1):
        sa = a_list[i-1] - a_list[i]
        if sa < 0:
            sa = -1 * sa
        total += sa
    return total

def get_listpattern(lst):
    if len(lst) == 1:
        return [lst]
    else:
        lst_pattern = []
        for i in range(len(lst)):
            new_lst_head = lst[i]
            if i == 0:
                new_lst_other_items = lst[1:]
            elif i == len(lst) - 1:
                new_lst_other_items = lst[:i]
            else:
                new_lst_other_items = lst[0:i] + lst[i+1:]
            new_lst_others = get_listpattern(new_lst_other_items)
            for new_lst_other in new_lst_others:
                lst_pattern.append([new_lst_head] + new_lst_other)
        return lst_pattern

def solve(a_list):
    a_list_pattern = get_listpattern(a_list)
    a_list_patterns_sa = map(calc_tonari_sa_total, a_list_pattern)
    return max(a_list_patterns_sa)

def main():
    while 1:
        input_line = input()
        n = int(input_line)
        a_list = []
        for i in range(n):
            a_list.append(int(input()))
        print(solve(a_list))

if __name__ == "__main__":
    main()
