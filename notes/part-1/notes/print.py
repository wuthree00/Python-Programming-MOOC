# this section covers how to display information in Python using the 'print()' function, along with my comments explaining how to understand the functions

## printing strings
print("Hi there!")
print("2 + 2 * 10")

## printing numbers
print(2 + 2 * 10)

# numbers and strings cannot be directly printed together
# convert numbers to string format with str()
name = "Alice"
age = 20
print("Name: " + name + ", Age: " + str(age))
print(f"Name: {name}, Age: {age}")   # using f indicates indicates that everything inside the {brackets} will be carried out
# numbers can be divided using the division operator /, but attempting to divide a string by a number causes an error
# the comma notation in the print command automatically inserts a space around the different comma-separated parts

# using print() adds a new line by default. add end="" to continue on the same line
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4)

# how to request user's input and print their input
name = input("What is your name? ")
print("Your name: " + name)
# Read as: the variable called “name” will store the input from the user after the computer asks the user “What is your name?”
# For integer values the + operator means addition, but for string values it means concatenation, or "stringing together"

# printing with f-strings
# if print with ‘normal’ commas:
print("Hi", name, ", you are", age, "years old. You live in", city, ".")
# [OUTPUT]: Hi Mark , you are 37 years old. You live in Palo Alto. ## note the extra space after 'Mark' ##

# if print with f-string:
print(f"Hi {name}, you are {age} years old. You live in {city}.")
# [OUTPUT]: Hi Mark, you are 37 years old. You live in Palo Alto.

## iterative calculations
# used to repeatedly add a number to the current value of 'sum'
sum += number
sum = sum + number
# "Reusing" a variable only makes sense when there is a need to temporarily store things of a similar type and purpose, for example when summing numbers

