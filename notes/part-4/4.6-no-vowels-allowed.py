## Please write a function named no_vowels, which takes a string argument.
## The function returns a new string, which should be the same as the original but with all vowels removed.
# You can assume the string will contain only characters from the lowercase English alphabet a...z.

#-----------------------------------
# An example of expected behaviour:
# my_string = "this is an example"
# print(no_vowels(my_string))

# Sample output
# ths s n xmpl
#-----------------------------------


## Solution:
def no_vowels(my_string):
    vowels = "aeiou"
    vowelless_string = "" #set my new string as blank, i will build a new string based on the original string, adding in only non-vowels
    for i in my_string:
        if i not in vowels:
            vowelless_string += i
    return vowelless_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
