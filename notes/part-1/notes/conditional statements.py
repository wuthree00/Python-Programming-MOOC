# This page covers the basics of conditional statements & also Boolean expressions in the university of helsinki's python programming MOOC
# https://programming-25.mooc.fi/part-1/5-conditional-statements

## Comparison Operators
| Operator | Meaning                       | Example   | Result |
|----------|-------------------------------|-----------|--------|
| ==       | Equal to                      | 3 == 3    | True   |
| !=       | Not equal to                  | 3 != 5    | True   |
| >        | Greater than                  | 3 > 2     | True   |
| >=       | Greater than or equal to      | 3 >= 3    | True   |
| <        | Less than                     | 3 < 5     | True   |
| <=       | Less than or equal to         | 3 <= 3    | True   |
# note: python evaluates the expression regarding whether it is True or False ^

## Comparison Operators – False Examples
| Operator | Example | Evaluates to |
|----------|---------|--------------|
| ==       | 3 == 5  | False        |
| !=       | 3 != 3  | False        |
| >        | 3 > 5   | False        |
| >=       | 2 >= 3  | False        |
| <        | 5 < 3   | False        |
| <=       | 2 <= 1  | False        |
# note: this is an example where the expression is evaluated to be 'False'


## Basic If Statement
a = 3
if a < 5:
    print("a is less than 5")

# Example - input:
students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

if students % size == 0:
    print(f"Number of groups formed: {students // size}")
else:
    print(f"Number of groups formed: {students // size + 1}")

# Example - output:
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2

# How many students on the course? 11
# Desired group size? 3
# Number of groups formed: 4


# Example - skipping a specific string
name = input("Please tell me your name: ")
if name != "Jerry":        # the condition: if the person is NOT Jerry, they'll be asked how many portions + told the total cost
    portions = float(input("How many portions of soup? "))
    print(f"The total cost is {portions * 5.9}")           
print("Next please!")

# Example - output:
Please tell me your name: Kramer    # the string inputted is NOT Jerry hence the programme proceeds with subsequent questions
How many portions of soup? 2
The total cost is 11.8
Next please!


## Boolean statements
# Boolean expression: the test/question (eg: a < 5)
# Boolean value: the answer (True or False)

# Example: to store the result of the Boolean expression, which is “True” (which is also called the Boolean value), in the variable called "condition":
a = 3
condition = a < 5   # "a < 5" is the Boolean expression. the result of "a < 5" is TRUE because a equals to 3, and this result is the Boolean VALUE
print(condition)    # the Boolean value is already deemed to be "True" above; the Boolean value is stored as "True"
if condition:
    print("a is less than 5")

#[OUTPUT]:
# True
# a is less than 5

# Example: directly using the keyword True/False (which are Boolean values)
condition = True
if condition:
    print("This is printed every time.")
# [OUTPUT]:
# This is printed every time.
