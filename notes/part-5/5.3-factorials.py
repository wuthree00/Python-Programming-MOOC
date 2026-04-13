## Please write a function named factorials(n: int), which returns the factorials of the numbers 1 to n in a dictionary.
## The number is the key, and the factorial of that number is the value mapped to it.

# A reminder: the factorial of the number n is written n! and is calculated by multiplying the number by each integer smaller than itself.
# For example, the factorial of 4 is 4 * 3 * 2 * 1 = 24.

# An example of the function in action:
#-------------------#
# k = factorials(5) #
# print(k[1])       #
# print(k[3])       #
# print(k[5])       #
#-------------------#

# Sample output:
#-----#
# 1   #
# 6   #
# 120 #
#-----#


## Solution:
def factorials(n: int):
    my_dictionary = {}

    for i in range(1, n+1):
        if i == 1:
            my_dictionary[i] = 1
        else:
            my_dictionary[i] = my_dictionary[i-1] * (i)
    return my_dictionary
    #note: for 'else' we cannot use "my_dictionary[i] = my_dictionary[i] * (i-1)" because my_dictionary[i] is not yet defined when at i=2
    #hence, must first use my_dictionary[i-1] to get the previous value my_dictionary[1] which already defined (it is '1')

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])



## The model solution provided:
# def factorials(n: int):
#     result = {}
#     result[1] = 1
#     for i in range(2, n + 1):
#         result[i] = result[i-1] * i
#     return result
