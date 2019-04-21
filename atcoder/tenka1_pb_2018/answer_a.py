
"""
英小文字からなる長さ 2 または 3 の文字列 S が与えられます。長さが 2 の場合はそのまま、長さが 3 の場合は逆順にして出力してください。

制約
S の長さは 2 または 3 である
S は英小文字からなる
"""
def main():
    while 1:
        input_line = input()
        if len(input_line) == 2:
            print(input_line)
        else:
            print(input_line[::-1])

if __name__ == "__main__":
    main()
