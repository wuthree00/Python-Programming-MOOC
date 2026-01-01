## Please write a function named shape, which takes four arguments.
## The first two parameters specify a triangle, as above, and the character used to draw it.
## The first parameter also specifies the width of a rectangle, while the third parameter specifies its height.
## The fourth parameter specifies the filler character of the rectangle.
## The function prints first the triangle, and then the rectangle below it.

# The function should call the function line from the exercise above for the actual printing out.
# Copy your solution to that exercise above the code for this exercise.
# Please don't change anything in the line function.

## Some examples:
# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")

## Sample output
# X
# XX
# XXX
# XXXX
# XXXXX
# *****
# *****
# *****

# o
# oo
# ++
# ++
# ++
# ++

# .
# ..
# ...


## Solution:
def line(a, b):
    if b != "":
        print(a*b[0])
    else:
        print(a*"*")

def shape(width, char1, height, char2):
    i = 1
    while i <= width:
        line(i, char1)
        i += 1

    j = 0
    while j < height:
        line(width, char2)
        j += 1
