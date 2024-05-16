def main(input1, input2):
    nums = sorted(map(int, input2.split()), reverse=True)
    return " ".join((str(sum(nums[::2])), str(sum(nums[1::2]))))

def testing():
    assert main('2', '-1 0') == '0 -1'
    assert main('4', '5 7 3 2') == '10 7'
    assert main('3', '8 6 4') == '12 6'

if __name__ == "__main__":    
    testing()
    print(main(input(), input()))


