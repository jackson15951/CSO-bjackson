'''
Corin Chepko
2/28/24
Kattis Problem: Oddities https://open.kattis.com/problems/oddities
Algorithm Steps:
    Read the number, 'num_numbers', of numbers to evaluate for even or oddness
    for num_numbers:
        read in the number
        check if the number is even or odd
        construct an answer "x is even" or "x is odd", 
            x being the number in question
'''
num_numbers = int(input()) 
                        
for i in range(num_numbers):
    number = int(input()) 

    if number%2 == 0: ans = "%s is even" %number
    else: ans = "%s is odd" %number
    
    print(ans)