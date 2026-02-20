## Please write a function named anagrams, which takes two strings as arguments.
## The function returns True if the strings are anagrams of each other.
## Two words are anagrams if they contain exactly the same characters.

# Some examples of how the function should work:
#----------------------------------------------------------
# print(anagrams("tame", "meta")) # True
# print(anagrams("tame", "mate")) # True
# print(anagrams("tame", "team")) # True
# print(anagrams("tabby", "batty")) # False
# print(anagrams("python", "java")) # False
# Hint: the function sorted can be used on strings as well.
#----------------------------------------------------------


## Solution:
def anagrams(a,b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    return a_sorted == b_sorted

if __name__ == "__main__":
    print(anagrams("tame", "meta"))
    print(anagrams("tame", "mate"))
    print(anagrams("tame", "team"))
    print(anagrams("tabby", "batty"))
    print(anagrams("python", "java"))


## ALTERNATIVELY, THIS COULD WORK TOO:
def anagrams(a,b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    if a_sorted == b_sorted:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "meta"))
    print(anagrams("tame", "mate"))
    print(anagrams("tame", "team"))
    print(anagrams("tabby", "batty"))
    print(anagrams("python", "java"))
