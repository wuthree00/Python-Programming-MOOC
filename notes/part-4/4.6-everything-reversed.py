## Please write a function named everything_reversed, which takes a list of strings as its argument.
## The function returns a new list with all of the items on the original list reversed.
## Also the order of items should be reversed on the new list.

# An example of how the function should work:
# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)

## Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']


## Solution:
def everything_reversed(my_list):
    reversed_letters = []
    final_list = []

    #first reverse the letters in each name
    for word in my_list:
        reversed_letters.append(word[::-1]) #reverses letters in each word, adding it to new list

    #now reverse the ORDER of the list itself
    i = len(reversed_letters)-1 #start from last index of list
    while i>= 0:
        final_list.append(reversed_letters[i]) #add each reversed word to final_list, starting from end of reversed_list
        i -= 1
    return final_list

if __name__ == "__main__":
    # here the global variable is assigned
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)


## Model solution:
#-----------------------------------------
#def everything_reversed(my_list: list):
#    new_list = []
#    for my_string in my_list:
#        new_list.append(my_string[::-1])
#    return new_list[::-1]
# Write your solution here
#-----------------------------------------
