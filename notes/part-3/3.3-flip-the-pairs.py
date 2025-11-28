## Please write a program which asks the user to type in a number.
## The program then prints out all the positive integer values from 1 up to the number.
## However, the order of the numbers is changed so that each pair or numbers is flipped.
## That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

## Sample output
# Please type in a number: 5
# 2
# 1
# 4
# 3
# 5

## Sample output
# Please type in a number: 6
# 2
# 1
# 4
# 3
# 6
# 5


## Solution
number = int(input("Please type in a number: "))

index = 1

while 0 < index <= number:
    bigger = index+1
    if bigger <= number:
        print(bigger)
    print(index)
    index += 2

## my reasoning:
# /cycle starts. take that the number = 5
# while number is greater or = to index
# save the value of 1 more than the index as 'bigger'
# if 'bigger' value is still less than or equal to the input number, print it. now print index. add 2 to current index
# cycle repeats until bigger value is more than the number (this is when index = 5, where bigger value will be 6)
# if 'bigger' value is more than number (this only happens when index = 5), DONT print this 'bigger' value and skip to printing the index (which is 5).
# since the next index will be more than the inputted number 5, the while loop no longer continues.
