## Please write a function named create_tuple(x: int, y: int, z: int),
## which takes three integers as its arguments,
## and creates and returns a tuple based on the following criteria:

#---------------------------------------------------------------------#
# 1. The first element in the tuple is the smallest of the arguments  #
# 2. The second element in the tuple is the greatest of the arguments #
# 3. The third element in the tuple is the sum of the arguments       #
#---------------------------------------------------------------------#

# An example of its use:
# if __name__ == "__main__":
#     print(create_tuple(5, 3, -1))

# Sample output:
# (-1, 5, 7)


## Solution:
def create_tuple(x: int, y: int, z: int):
    #(smallest, largest, sum)
    small_to_big = sorted([x, y, z])
    return (small_to_big[0], small_to_big[-1], sum(small_to_big))

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))



## The model solution provided:
# def create_tuple(x: int, y: int, z: int):
#     """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
#     smallest = min([x, y, z])
#     greatest = max([x, y, z])
#     sum = x + y + z # sum([x, y, z]) also works
 
#     return (smallest, greatest, sum)
