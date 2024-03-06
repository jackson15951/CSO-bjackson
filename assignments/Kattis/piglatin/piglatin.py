'''
Corin Chepko
3/6/24
Kattis problem: Piglatin https://open.kattis.com/problems/piglatin
Algorithm Steps:
    While reading lines in until end of file:
        separate the line in words
        for each word:
            convert to piglatin by:
                if word begins with consonant:
                    move all letters before vowel to end of word and add 'ay'
                else:
                    add 'yay' to end of word
            print piglatin line by joining words using join method
'''
import sys

def piglatin(word):
    vowels = ['a','e','i','o','u','y']
    if word[0] in vowels:
        word = word + 'yay'
    else:      
        index = 0
        for i in word:
            if i in vowels: 
                beg = word[0:index]
                word = word[index::] + beg + 'ay'
                break
            index = index + 1
    return word

for words in sys.stdin:
    if not words:
        break

    translation = []
    words = words.split()
    for word in words:
        translation.append(piglatin(word))
    print(' '.join(translation))

