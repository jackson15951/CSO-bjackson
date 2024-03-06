'''
Corin Chepko
2/23/24
Kattis Problem: Ullen etc...:   https://open.kattis.com/problems/ullendullendoff
Algorithm Steps:
    input number of friends and convert to int
    input names separted by a space using .split() method
    if( there are more than 14 friends, pick the 13th friend (or number 12 if starting from 0))
    else:
        Take 13 % N_friends name as friend, or (13 % N-friends) - 1 if zero based 
'''


n_friends = int(input())
names = input().split()

if n_friends >= 13: print(names[12])
else:               
    position = 13%n_friends - 1
    print(names[position]) 
