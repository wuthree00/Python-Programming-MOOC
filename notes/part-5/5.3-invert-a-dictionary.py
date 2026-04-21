## Please write a function named invert(dictionary: dict), which takes a dictionary as its argument.
## The dictionary should be inverted in place so that values become keys and keys become values.

# An example of its use:
#--------------------------------------------------------#
# s = {1: "first", 2: "second", 3: "third", 4: "fourth"} #
# invert(s)                                              #
# print(s)                                               #
#--------------------------------------------------------#

# Sample output:
# {"first": 1, "second": 2, "third": 3, "fourth": 4}

# NB: the principles regarding lists covered here also hold for dictionaries passed as arguments.


## My solution:
def invert(dictionary: dict):
    new_dict = {} #remember dictionary[key] = value
    for key, value in dictionary.items():
        new_dict[value] = key

    dictionary.clear()
    dictionary.update(new_dict)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)


## The model solution provided:
# def invert(dictionary: dict):
#     copy = {}
#     for key in dictionary:
#         copy[key] = dictionary[key]
#     for key in copy:
#         del dictionary[key]
#     for key in copy:
#         dictionary[copy[key]] = key
