## Please write a function named most_common_character, which takes a string argument.
## The function returns the character which has the most occurrences within the string.
## If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

# An example of expected behaviour:
# first_string = "abcdbde"
# print(most_common_character(first_string))

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))

# Sample output
# b
# e


## Solution:
def most_common_character(my_string):
    best = my_string[0] #first character in string is saved as best
    for character in my_string:
        if my_string.count(character) > my_string.count(best):
            best = character
    return best

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
