## Please write a function named oldest_person(people: list),
## which takes a list of tuples as its argument.
## In each tuple, the first element is the name of a person, and the second element is their year of birth.
## The function should find the oldest person on the list and return their name.

# An example of the function in action:
#------------------------------#
# p1 = ("Adam", 1977)          #
# p2 = ("Ellen", 1985)         #
# p3 = ("Mary", 1953)          #
# p4 = ("Ernest", 1997)        #
# people = [p1, p2, p3, p4]    #
#                              #
# print(oldest_person(people)) #
#------------------------------#

# Sample output:
# Mary


## Solution:
def oldest_person(people: list):
    #find the smallest year
    oldest_person = people[0] #start w first person as oldest
    for person in people:
        if person[-1] < oldest_person[-1]: #compare birth years
            oldest_person = person
    return oldest_person[0]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))


  
## The model solution provided:
# def oldest_person(people: list):
#     oldest = people[0]
#     for person in people:
        ## comparing the year of birth of the oldest known person and the person in turn
#         if person[1] < oldest[1]:
#             oldest = person
 
#     return oldest[0]
