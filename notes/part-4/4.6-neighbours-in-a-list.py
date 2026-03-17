## Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1.
## So, items 1 and 2 would be neighbours, and so would items 56 and 55.
## Write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

# For eg in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

# An example function call:
#----------------------------------------------
# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))

# Sample output
# 4
#----------------------------------------------


## Solution:
def longest_series_of_neighbours(my_list):
    #check if the second value is one more or less than first value
    #if it is, add it to the list variable
    #if not, check if length of list variable is longer than current longest length
    #if this is the longest variable, set this length as the longest length
    #check the next index, repeat the process until end of the list is reached
    longest_length = 0
    current_length = 1
    i = 0
    while i < len(my_list)-1:
        if my_list[i] + 1 == my_list[i+1] or my_list[i] - 1 == my_list[i+1]: #if next value is 1 more or less than current
            current_length += 1
        else: #only check if length of current list is longest when the consecutive series ends
            if current_length > longest_length:
                longest_length = current_length
            current_length = 1 #reset current_length to 1 to restart checks for next series
        i += 1
    if current_length > longest_length:
        longest_length = current_length
    return longest_length


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
