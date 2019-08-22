def singleFlipPossible(aString):

    zeros = 0
    ones = 0

    # Traverse through given string and
    # count numbers of 0's and 1's
    for i in range(0, len(aString)):

        achar = aString[i];
        if (achar == '0'):
            zeros = zeros + 1
        else:
            ones = ones + 1

    # Return true if any of the two
    # counts is 1
    return (zeros == 1 or ones == 1)

inputStr=str(input())

if(singleFlipPossible(inputStr)):
    print("YES",end='')
else:
    print("NO",end='')
