## Please write a function named same_chars, which takes one string and two integers as arguments.
## The integers refer to indexes within the string.
## The function should return True if the two characters at the indexes specified are the same.
## Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.

# Some examples of how the function is used:

# same characters m and m
# print(same_chars("programmer", 6, 7)) # True

# different characters p and r
# print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
# print(same_chars("programmer", 0, 12)) # False


## Solution:
def same_chars(word, index1, index2):
    if index1 < 0 or index2 < 0:
        return False
    if index1 >= len(word) or index2 >= len(word):
        return False
    if word[index1] == word[index2]:
        return True
    else:
        return False

# Test the function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 0, 12))
