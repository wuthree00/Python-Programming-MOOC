## Please write a function named distinct_numbers, which takes a list of integers as its argument.
## The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.

#---------------------------------------------
# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]
#---------------------------------------------


## Solution:
def distinct_numbers(my_list):
    sorted_list = sorted(my_list) #this saves the list, sorted from small to big
    new_list = []
    for i in sorted_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]

# my approach was to create a new list from scratch, adding in only NON-duplicate numbers
