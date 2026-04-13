## Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary.
## The keys of the dictionary should be the numbers between start_index and end_index inclusive

# The value mapped to each key should be the key times ten.

# For example:
#---------------------#
# d = times_ten(3, 6) #
# print(d)            #
#---------------------#

# Sample output
#------------------------------#
# {3: 30, 4: 40, 5: 50, 6: 60} #
#------------------------------#


## Solution:
def times_ten(start_index: int, end_index: int):
    my_dictionary = {}
    for i in range(start_index, end_index + 1):
        my_dictionary[i] = i * 10
    return my_dictionary #MUST return because this line is part of a function which i am defining exactly how it should be used!
    #if 'return' is not 'forced' when im defining how to this function should be used, using this function (below for eg) will not work cos this function isnt set to return anything, so it will return 'None'

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)
