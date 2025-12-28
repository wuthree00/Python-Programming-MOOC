## Please write a function named square_of_hashes, which draws a square of hash characters.
## The function takes one argument, which determines the length of the side of the square.

# The function should call the function line from the exercise above for the actual printing out.
# Copy your solution to that exercise above the code for this exercise.
# Please don't change anything in the line function.

# Some examples:
# square_of_hashes(5)
# print()
# square_of_hashes(3)

## Sample output
# #####
# #####
# #####
# #####
# #####

# ###
# ###
# ###


## Solution:
def line(a, b):
    if b != "":
        print(a*b[0])
    else:
        print(a*"*")

if __name__ == "__main__":
    line(7, "")

def square_of_hashes(size):
    row = size
    while row > 0:
        line(size, "#")
        row -= 1

if __name__ == "__main__":
    square_of_hashes(3)
