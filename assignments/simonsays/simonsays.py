'''
- A game of Simon says
- First gets the num of commands
- Then gets the commands
- If Simon says, is in the command, it will print the command, excluding Simon says
- If Simon says, is not in the command, it will print nothing
'''

def main(test, test_lines): 
    lines = input() if test != True else test_lines[0] # gets the num of commands
    result = []

    for i in range(int(lines)):
        text = input() if test != True else test_lines[i+1]
        if ("Simon says") in text: result.append(" ".join(text.split(" ")[2:])) # If Simon says, is in the command, it will add the command to results, excluding 'Simon says'
    
    return '\n'.join(result)


def testing():
    assert main(True, ['1', 'Simon says dance.']) == 'dance.'
    assert main(True, ['3', 'Simon says swim.', 'Have a party.', 'Do Nothing']) == 'swim.'
    assert main(True, ['4', 'Simon says have a party.', 'Do Nothing', 'Simon says dance.', 'Simon says do something.']) == 'have a party.\ndance.\ndo something.'

testing()       
print(main(False, []))

