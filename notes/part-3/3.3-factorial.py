## Please write a program which asks the user to type in an integer number.
## If the user types in a number equal to or below 0, the execution ends.
## Otherwise the program prints out the factorial of the number.

# The factorial of a number involves multiplying the number by all the positive integers smaller than itself.
# In other words, it is the product of all positive integers less than or equal to the number.
# For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

# Some examples of expected behaviour:

## Sample output
# Please type in a number: 3
# The factorial of the number 3 is 6
# Please type in a number: 4
# The factorial of the number 4 is 24
# Please type in a number: -1
# Thanks and bye!

## Sample output
# Please type in a number: 1
# The factorial of the number 1 is 1
# Please type in a number: 0
# Thanks and bye!


## Solution
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        factorial = 1
        next_number = number
        
        while next_number > 0:
            factorial *= next_number #factorial = factorial * next_number
            next_number -= 1   # ← THIS is the update every loop
        print(f"The factorial of the number {number} is {factorial}")

            #eg if no. = 5, then factorial = 1 * 5
            #next_number =4
            #then factorial = 1 * 5 * 4

            #until 1 * 5 * 4 * 3 * 2 * 1
            #then finally number = 0, so it breaks and goes back to 'while True'
