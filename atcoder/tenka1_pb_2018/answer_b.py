import sys

"""
高橋君は最初 A 枚、青木君は最初 B 枚のクッキーを持っています。 二人は、高橋君からはじめて交互に、以下の操作を繰り返します。

自分が持っているクッキーの枚数が奇数なら、自分が持っているクッキーを 1 枚食べ、偶数なら何もしない。その後、自分が持っているクッキーの半分を相手に渡す。
合計 K 回の操作を行った後の、高橋君と青木君が持っているクッキーの枚数をそれぞれ求めてください。

制約
1≤A,B≤109
1≤K≤100
A,B,K は整数である
入力
入力は以下の形式で標準入力から与えられる。

A B K
出力
合計 K 回の操作を行った後の、高橋君と青木君が持っているクッキーの枚数を順に出力せよ。
"""

# x回目のターン, aが実行者、bが受け取るだけの人
def turn_x(a, b):
    # step1. 奇数なら食べる
    if (a % 2 == 1):
        a -= 1
    # step2. 半分をあげる
    next_a = int(a / 2)
    next_b = b + int(a / 2)
    return next_a, next_b

def solve(a0, b0, k):
    a = a0
    b = b0
    for i in range(k):
        if (i % 2 == 0): # 先行、高橋
            next_a, next_b = turn_x(a, b)
        else: # 後攻、青木
            next_b, next_a = turn_x(b, a)
        a = next_a
        b = next_b
    return a, b


def main():
    while 1:
        input_line = input()
        in_splitted = input_line.split()
        a0 = int(in_splitted[0])
        b0 = int(in_splitted[1])
        k = int(in_splitted[2])
        after_a, after_b = solve(a0, b0, k)
        print(f'{after_a} {after_b}')


if __name__ == "__main__":
    main()
