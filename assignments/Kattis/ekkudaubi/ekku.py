'''
Written by: Corin Chepko
Date: 2/7/24
Program: Kattis ekkidaubi problem: https://open.kattis.com/problems/ekkidaudi
Algorithm steps:
    input line1a and line1b, using .split(|) method
    input line2a and line2b, using .split(|) method
    add line1a to line1a for first word
    add line2a to line2b for second word
    print both words
'''

line1a, line1b = input().split('|')
line2a, line2b = input().split('|')

first = line1a+line2a
second = line1b+line2b

print(first, second)
