## Please write a program which asks the user to type in a string.
## The program then prints out all the substrings which begin with the first character, from the shortest to the longest.
# Have a look at the example below.

## Sample output
# Please type in a string: test
# t
# te
# tes
# test


## Solution
word = input("Please type in a string:")
a = 1

while a <= len(word):
    print(word[0:a])
    a += 1
