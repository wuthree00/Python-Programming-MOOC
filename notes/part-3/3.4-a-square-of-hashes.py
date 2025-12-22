## Please write a function named hash_square(length), which takes an integer argument.
## The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

#--------------#
# hash_square(3)
# print()
# hash_square(5)
#--------------#

## Sample output
 ###
 ###
 ###

 #####
 #####
 #####
 #####
 #####


## Solution:
def hash_square(number):
    count = number
    while count > 0:
        print("#"*number)
        count -= 1

# Test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(3)
