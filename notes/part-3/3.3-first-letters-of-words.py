## Please write a program which asks the user to type in a sentence.
## The program then prints out the first letter of each word in the sentence, each letter on a separate line.

# An example of expected behaviour:

## Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w


## Solution
sentence = input("Please type in a sentence: ")
print(sentence[0]) #print 1st character

index = 0

while index < len(sentence) - 1:
    if sentence[index] == " ":
        print(sentence[index + 1])
        #print the 1st letter after this space
    index += 1
