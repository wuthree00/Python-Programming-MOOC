## Please write a program which asks for the user's name.
# If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost.
# The price of a single portion is 5.90.

# Two examples of the program's execution:

## Sample output
# Please tell me your name: -> input: 'Kramer'
# How many portions of soup? -> input: '2
# The total cost is 11.8
# Next please!

## Sample output
# Please tell me your name: -> input: 'Jerry
# Next please!


## Solution:
name = input("Please tell me your name:  ")
if name != "Jerry":
    portions = int(input("How many portions of soup? "))
    cost = 5.9 * portions
    print("The total cost is", cost)
print("Next please!")


## Solution: (24 Feb 2026 revision + update)
name = input("Please tell me your name: ")
if name != "Jerry":
    soup = int(input("How many portions of soup?"))
    print(f"The total cost is {soup*5.9}")
print("Next please!")
