## Please write a function named all_the_longest, which takes a list of strings as its argument.
## The function should return a new list containing the longest string in the original list.
## If more than one are equally long, the function should return all of the longest strings.

# The order of the strings in the returned list should be the same as in the original.

#-------------------------------------------------------------------
# my_list = ["first", "second", "fourth", "eleventh"]
# result = all_the_longest(my_list)
# print(result) # ['eleventh']

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
# result = all_the_longest(my_list)
# print(result) # ['dorothy', 'richard']
#-------------------------------------------------------------------


## Solution:
def all_the_longest(my_list):
    best = [my_list[0]] #the first string is saved as best; [] converts it to list
    for i in my_list: #for the string values in my_list (which are i)
        if len(i) > len(best[0]): #if the length of i string is > length of the first value in the list 'best'
            best = [i] #save the string i as the only value in the list 'best'
        if len(i) == len(best[0]): #if length of i string = length of first value in the list 'best'
            if i not in best: #if the string i is not already in the list 'best'
                best.append(i) #add string i to the list 'best'
    return best


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']
    
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
