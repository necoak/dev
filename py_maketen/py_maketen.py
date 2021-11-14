#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys
import itertools

def maketen1(nums, operators):
    num_indx = 0
    ans = nums[num_indx]
    num_indx +=1
    for operator in operators:
        if operator == '+':
            ans += nums[num_indx]
        elif operator == '-':
            ans -= nums[num_indx]
        elif operator == '*':
            ans *= nums[num_indx]
        elif operator == '/':
            if ans % nums[num_indx]:
                return False
            ans //= nums[num_indx]
        num_indx += 1
    # print(nums, operators, ans)
    return ans == 10


def maketen(innums):
    num_patterns = list(itertools.permutations(innums, 4))
    
    operators = ['+', '-', '*', '/']
    operator_patterns = list(itertools.product(operators, repeat=3))

    for num_pattern in num_patterns:
        for operator_pattern in operator_patterns:
            result1 = maketen1(num_pattern, operator_pattern)
            if result1:
                result_text = '((%d %s %d) %s %d) %s %d' % (
                    num_pattern[0], operator_pattern[0],
                    num_pattern[1], operator_pattern[1],
                    num_pattern[2], operator_pattern[2],
                    num_pattern[3])
                return(True, result_text)

    return (False, '')

@click.command()
def cmd():
    click.echo('Make10: 4つの整数の四則演算で10ができるか？')
    click.echo('4つの1桁整数をスペース区切りで入力してください')
    intext = input('> ')
    innum_texts = intext.split()
    innums = []
    if len(innum_texts) != 4:
        print('整数は4つのみ入力してください')
        sys.exit(1)
    for innum_text in innum_texts:
        if innum_text not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('0から9の整数のみ入力してください')
            sys.exit(1)
        innums.append(int(innum_text))
    result = maketen(innums)
    if result[0]:
        print(result[1])
    else:
        print('10にできる計算式はありません')


if __name__ == '__main__':
    cmd()
