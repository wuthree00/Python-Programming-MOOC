## Write a function named shortest, which takes a list of strings as its argument.
## The function returns whichever of the strings is the shortest.
## If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests).
## You may assume there will be no empty strings in the list.

#------------------------------------------------------------------
# my_list = ["first", "second", "fourth", "eleventh"]
# result = shortest(my_list)
# print(result)

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = shortest(my_list)
# print(result)

## Sample output:
# first
# Tim
#------------------------------------------------------------------


## Solution:
def shortest(my_list):
    best = my_list[0]      #this saves the first value (a string) in list as 'best'
    for i in my_list:      #note: i here is a STRING not integer. The program will run through all the ‘i’s which are the diff values in the list!
        if len(i) < len(best):     #if the length of the string i < current shortest integer
            best = i   #rmb ‘i’ is a string not integer!
    return best

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
