## Please write a function named sum_of_positives, which takes a list of integers as its argument.
## The function returns the sum of the positive values in the list.

#------------------------------------
# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)

## Sample output:
# The result is 9
#------------------------------------


## Solution:
def sum_of_positives(my_list):
    for x in my_list:
        positive_list = [x for x in my_list if x > 0]
        return sum(positive_list)
# note to self: recall that when i define my own function, the stuff i write under the definition gets carried out when i use this function that i wrote!

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
