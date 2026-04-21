# These are the arithmetic operations used in python as introduced in the MOOC
# https://programming-25.mooc.fi/part-1/4-arithmetic-operations

x = 27 # data in x is stored as an integer
y = 15 # data in y is stored as an integer

# basic operations
print(f"{x} + {y} = {x + y}")    # addition
print(f"{x} - {y} = {x - y}")    # subtraction
print(f"{x} * {y} = {x * y}")    # multiplication
print(f"{x} / {y} = {x / y}")    # floating-point division
print(f"{x} // {y} = {x // y}")  # integer division; number is rounded DOWN
print(f"{x} % {y} = {x % y}")    # modulo; the remainder after division
print(f"{x} ** 2 = {x ** 2}")    # exponentiation; basically x^2

# working with floats (and integers)
cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))  # this stores the data as a whole number integer
lunch = float(input("The price of a typical student lunch? "))                         # this stores the data as a float with decimals
groceries = float(input("How much money do you spend on groceries in a week? "))       # this stores the data as a float with decimals

print("Average food expenditure:")
print(f"Daily: {(lunch * cafeteria + groceries) / 7} euros")      # integers and floats can be used and run in the same line
print(f"Weekly: {(lunch * cafeteria + groceries)} euros")
