## Please write a function named squared, which takes a string argument and an integer argument, and prints out a square of characters as specified by the examples below.

#----------------------#
# squared("ab", 3)
# print()
# squared("aybabtu", 5)
#----------------------#

## Sample output
# aba
# bab
# aba

# aybab
# tuayb
# abtua
# ybabt
# uayba


## Solution:
def squared(text, number):
    i = 0
    longtext = text*number*number #the text appears that specific number of times
    while i < number:
        row = longtext[(i*number):(i*number+number)]
        print(row)
        i += 1

if __name__ == "__main__":
    squared("ab", 3)
