## Please write a function named length_of_longest, which takes a list of strings as its argument.
## The function returns the length of the longest string.

#------------------------------------------------------------------
# my_list = ["first", "second", "fourth", "eleventh"]
# result = length_of_longest(my_list)
# print(result)

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# result = length_of_longest(my_list)
# print(result)

## Sample output:
# 8
# 7
#------------------------------------------------------------------


## Solution:
def length_of_longest(my_list):
    best = 0
    for i in my_list:
        if len(i) > best:
            best = len(i)
    return best

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)
