#!/usr/bin/env python3
# Atcoder necoak answer
# https://atcoder.jp/contests/abc029/tasks/abc029_c

n_text = input()
n =int(n_text)

chrs = ['a', 'b', 'c']

def bluteforce(text, zanlen):
    if zanlen == 0:
        return [text]
    
    texts = []
    for c in chrs:
        texts_x = bluteforce(text + c, zanlen-1)
        texts.extend(texts_x)
    return texts

result_list = bluteforce('', n)
for result in result_list:
    print(result)

