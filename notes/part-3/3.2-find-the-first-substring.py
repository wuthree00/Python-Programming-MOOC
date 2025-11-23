## Please write a program which asks the user to type in a string and a single character.
## The program then prints the first three character slice which begins with the character specified by the user.
## You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

# Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for.
# In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

## Sample output
# Please type in a word: mammoth
# Please type in a character: m
# mam

## Sample output
# Please type in a word: banana
# Please type in a character: n
# nan

## Sample output
# Please type in a word: tomato
# Please type in a character: x

## Sample output
# Please type in a word: python
# Please type in a character: n


## Solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = word.find(character)    #this means in word, find character, and save the index position number in the variable 'index'

if index + 3 <= len(word):
    print(word[index:index+3])
