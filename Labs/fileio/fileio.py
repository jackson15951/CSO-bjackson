"""
File I/O Lab
By: FIXME0

CSCI 110
Date: FIXME0

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""
import pathlib

totalInts = 10
my_path = pathlib.Path(__file__).parent.resolve()

def readData():
    intList = []
    # FIXME1 (20 points): #fixed#
    # Prompt user to input file name
    # open the file; read each number one line at a time;
    # and store it into intList list
    # close the file
    # return the intList
    
    filename = input('input file name: ')
    file = open(f"{my_path}/{filename}", 'r')
    for i in file.readlines(): intList.append(int(i))
    file.close()
    
    return intList


def sortListInAscendingOrder(lstInts):
    # FIXME2 #fixed#
    # sort lstInts list in ascending order
    return sorted(lstInts)


def sortListInDescendingOrder(lstInts):
    # FIXME3 #fixed#
    # sort lstInts in descending order
    return sorted(lstInts, reverse=True)


def printList(printFile, lstInts):
    for i in lstInts:
        # FIXME4 #fixed#
        # write each value one line at a time to file
        # handled by printFile object.
        printFile.write(str(i) + '\n')
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXME5 #fixed#
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXME6 #fixed#
    # Write the sorted list in descending order to the output file
    printFile.write("Numbers sorted in descending order:\n")
    printList(printFile, integers)
    
    
    # FIXME7 #fixed#
    # Print the largest number to the output file
    printFile.write("The largest number:\n")
    printList(printFile, str(max(integers)))

    # FIXME8 #fixed#
    # Print the smallest number to the output file
    printFile.write("The smallest number:\n")
    printList(printFile, str(min(integers)))

    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXME9 #fixed#
# Call main function if this module is run as the main module
main()