'''
Corin Chepko
3/15/24
Kattis Problem: Pet https://open.kattis.com/problems/pet
Alogorithm Steps:
    for 5 chef scores:
        input line of numbers, convert them to ints
        Sum those ints for the chef score
        Add that score to a list of chef scores
    Pick the top score and line number from the list of scores
    print line number (starting from 1) and winning score
'''

nums_list = []  

for _ in range(5): 
    nums = input().split()
    nums = list(map(int, nums))

    sum_nums = sum(nums) 
    nums_list.append(sum_nums)  

max_num = max(nums_list)
index = nums_list.index(max_num)

print(index+1, max_num)