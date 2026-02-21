## Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome.
## Palindromes are words which are spelled exactly the same backwards and forwards.

# Please also write a main program which asks the user to type in words until they type in a palindrome:

## Sample output:
#----------------------------------------------
# Please type in a palindrome: python
# that wasn't a palindrome
# Please type in a palindrome: java
# that wasn't a palindrome
# Please type in a palindrome: oddoreven
# that wasn't a palindrome
# Please type in a palindrome: neveroddoreven
# neveroddoreven is a palindrome!
#----------------------------------------------

# NB: the main program should not be within an if __name__ == "__main__": block


## Solution:
# this is where i define my own function
def palindromes(word):
    return word == word[::-1] #here, i have just created my own function!

# this is the 'main' programme
word = input("Please type in a palindrome: ")
while True:
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
    word = input("Please type in a palindrome: ")

# this is where i test whether my programme works
if __name__ == "__main__":
    palindromes("python")
