## Please write a function named box_of_hashes, which prints out a rectangle of hash characters.
## The function takes one argument, which specifies the height of the rectangle.
## The rectangle should be ten characters wide.

# The function should call the function line from the exercise above for the actual printing out.
# Copy your solution to that exercise above the code for this exercise.
# Please don't change anything in your line function.

# Some examples of how the function should work:
# box_of_hashes(5)
# print()
# box_of_hashes(2)

## Sample output
#  ##########
#  ##########
#  ##########
#  ##########
#  ##########

#  ##########
#  ##########


## Solution:
# Code of line function from previous exercise
def line(a, b):
    if b != "":
        print(a*b[0])
    else:
        print(a*"*")

# Test the function by calling it within the following block
if __name__ == "__main__":
    line(7, "")

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1

# Test the function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
