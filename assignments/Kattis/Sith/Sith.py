import sys

def solution(a, b, a_minus_b):
    if (a-b > 0):
        answer = "VEIT EKKI"
    elif (a-b == a_minus_b):
        answer = "JEDI"
    else:
        answer = "SITH"
    
    return answer

def test():
    assert solution(38, 68, 30) == "SITH"
    assert solution(69, 80, -11) == "JEDI"
    assert solution(67, 17, 50) == "VEIT EKKI"
    print("All test passed!")

def main():
    input()
    a = int(input())
    b = int(input())
    a_minus_b = int(input())
    answer = solution(a, b, a_minus_b)
    
    print(answer)

test()

main()
