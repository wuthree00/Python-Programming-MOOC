## The exercise contains the outline of the function first_character.
## Please complete it so that it prints out the first character of the string it takes as its argument.

# def first_character(text):

# testing the function:
# if __name__ == "__main__":
#     first_character('python')
#     first_character('yellow')
#     first_character('tomorrow')
#     first_character('heliotrope')
#     first_character('open')
#     first_character('night')

## Sample output
# p
# y
# t
# h
# o
# n


## Solution
def first_character(text):
    print(text[0:1])

#note that the below merely tests the function and is NOT graded for logic
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')
