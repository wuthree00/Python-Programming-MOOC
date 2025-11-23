## Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long,
## and which begin with the character specified by the user.
## You may assume the input string is at least three characters long.

## Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam
# mmo
# mot

## Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

# Hint the following example may give you some inspiration as to how this exercise could be tackled:

# ----------------------- #
# word = input("Word: ")  #
# while True:             #
#     if len(word) == 0:  #
#         break           #
#     print(word)         #
#     word = word[2:]     #
# ----------------------- #

## Sample output
# Word: mammoth
# mammoth
# mmoth
# oth
# h


## Solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index <= len(word) - 3:   #while there are at least 3 characters when starting from this index
    if word[index] == character:
        print(word[index:index+3])
    index += 1
