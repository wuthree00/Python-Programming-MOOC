## Please write a function named spruce, which takes one argument.
## The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

# Calling spruce(3) should print out:
# a spruce!
#   *
#  ***
# *****
#   *

# Calling spruce(5) should print out:
# a spruce!
#     *
#    ***
#   *****
#  *******
# *********
#     *

# NB: to the left of the spruce there should be exactly the right amount of whitespace.
# If the shape of the spruce looks correct, but the left edge of the tree is not touching the left edge of the text area in the terminal, the tests will not accept the solution.


## Solution:
def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        space = height - i
        print(" " * space + "*" * (2 * i -1))
        i += 1
    print(" " * (height - 1) + "*")

# Test the function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
