## Please write a function named list_sum which takes two lists of integers as arguments.
## The function returns a new list which contains the sums of the items at each index in the two original lists.
## You may assume both lists have the same number of items.

## An example of the function at work:
# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b)) # [8, 10, 12]


## Solution:
def list_sum(list1, list2):
    new_list = []
    i = 0
    while i < len(list1):
        new_list.append(list1[i] + list2[i]) #append the sum of integers at that specific index to the new list
        i += 1
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]

# first, define list_sum
# for the function list_sum, create a new list called new_list as i don't want to edit the original list
# create a while loop to loop through the index position of the lists using i, while i < length of the list
# within this while loop, append the sum of the integers at that index position to the new list
# finally return the new list
