## Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
## The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

## Sample output
# Word: testing
# ******************************
# *          testing           *
# ******************************

## Sample output
# Word: python
# ******************************
# *           python           *
# ******************************


## Solution
word = input("Word:")
length = len(word)                  #this is an integer
empty_space = 30 - length           #this is the number of spaces that'll be empty
each_side = (30 - length - 2)//2    #this is the number of spaces on each side

if (30 - length)%2 == 0:            #if number is even
    print("*"*30)
    print("*" + " " * each_side + word + " " * each_side + "*")
    print("*"*30)

else:                               #if number is not even (aka ODD)
    print("*"*30)
    print("*" + " " * (each_side+1) + word + " " * each_side + "*")
    print("*"*30)
