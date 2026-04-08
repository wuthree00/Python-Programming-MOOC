## Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.
## The functions should find and remove the smallest item in the list.
## You may assume there is a single smallest item in the list.

# The function should not have a return value - it should directly modify the list it receives as a parameter.
# An example of how the function works:

#----------------------------------#
# if __name__ == "__main__":       #
#     numbers = [2, 4, 6, 1, 3, 5] #
#     remove_smallest(numbers)     #
#     print(numbers)               #
#----------------------------------#
# Sample output:                   #
# [2, 4, 6, 3, 5]                  #
#----------------------------------#


## Solution:
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)


## Note: this is the model solution provided for this exercise:
#-------------------------------------#
# def remove_smallest(numbers: list): #
#     smallest = min(numbers)         #
#     numbers.remove(smallest)        #
#-------------------------------------#
