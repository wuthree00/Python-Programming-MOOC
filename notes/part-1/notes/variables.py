# These are the variables introduced in part 1 of the MOOC
# https://programming-25.mooc.fi/part-1/3-more-about-variables

# VARIABLES: they store and manipulate information
# TYPES of variables: strings, tntegers, floats, booleans


# assigning values to variables
name = "Alice"
age = 25               # note that this is an integer
height = 1.68          # in metres. note that this is a float


# integers vs strings
number1 = 100          # integer
number2 = "100"        # string
print(number1 + 50)    # this works, because number1 is an integer
# print(number2 + 50)  # ERROR, can't add string + integer together!


# converting between types --> use int() to convert a string to integer
days = int(input("How many days? "))
print(f"Seconds in that many days: {days * 24 * 60 * 60}")


# string concatenation vs commas in print
print("Your name is " + name)        # concatenation
print("Your name is", name)          # comma automatically adds space


# cannot mix string + number without converting
age = 20
# print("I am " + age + " years old")   # ERROR: cannot add strings with integer ('age' is the number 20)

# SOLUTION 1: convert number to string
print("I am " + str(age) + " years old") --> use str() to convert an integer to string
# SOLUTION 2: use commas --> remember that spaces are automatically added after commas!
print("I am", age, "years old")
# SOLUTION 3: use f-string --> CLEANEST WAY
print(f"I am {age} years old")


# floats --> data type that represents numbers with DECIMALS! (cf. integers, which are WHOLE numbers)
temperature = 36.5
print(f"Your body temperature is {temperature}") # this prints the temperature as a number w/ its decimal points
