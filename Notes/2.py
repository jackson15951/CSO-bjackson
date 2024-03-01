
'''
nums=[100,8.9, 999, 1000.5, -2000]

print('max=', max(nums))
print('min=', min(nums))

print('2 to the power 3 =', pow(2, 3))
print('2 to the power 3 =', 2**3)

print('hi', 'hello', end='=')
print('hi', 'hello', sep=' ', end='=')
print()

import sys

lin1, lin2 = input().split('|')
lin3, lin4 = input().split('|')

print(lin1+lin3,' ',lin2+lin4)



n1, n2, n3 = input('three nums plz: ').split(' ')
print(n1)
print(n2)
print(n3)
'''


xcords = [50, 100, 150, 200, 250, 300, 350]
ycords = [50, 100, 150]

# Functions
def expand(rows,cols):
    global xcords
    global ycords
    x = 350
    y = 150
    for i in range(cols):
        x = x + 50
        xcords.append(x)
    for i in range(rows):
        y = y + 50
        ycords.append(y)

expand(5,5)        
print(ycords)