## Please write a function named histogram, which takes a string as its argument.
## The function should print out a histogram representing the number of times each letter occurs in the string.
## Each occurrence of a letter should be represented by a star on the specific line for that letter.

# For example, the function call histogram("abba") should print out

# Sample output
#-------#
# a **  #
# b **  #
#-------#

# while histogram("statistically") should print out

# Sample output
#-------#
# s **  #
# t *** #
# a **  #
# i **  #
# c *   #
# l **  #
# y *   #
#-------#


## Solution:
def histogram(word):
    letters = {} #letters is a dictionary
    for letter in word:
        if letter not in letters:
            letters[letter] = 0 #for new letter, set count = 0
        letters[letter] += 1 #increase count for this letter

    for key, value in letters.items():
        print(f"{key} {value * "*"}")

if __name__ == "__main__":
    histogram("abba")
