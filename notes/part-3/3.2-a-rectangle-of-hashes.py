## Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

## Sample output
# Width: 10
# Height: 3
# ##########
# ##########
# ##########


## Solution
width = int(input("Width:"))
height = int(input("Height:"))

line = 1

while line <= height:
    print(width*"#")
    line += 1
