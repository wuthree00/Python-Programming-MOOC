'''
Please write a function named lottery_numbers(amount: int, lower: int, upper: int),
which generates as many random numbers as specified by the first argument.
All numbers should fall within the bounds lower to upper.
The numbers should be stored in a list and returned.
The numbers should be in ascending order in the returned list.

As these are lottery numbers, no number should appear twice in the list.
An example of how the function should work:

for number in lottery_numbers(7, 1, 40):
    print(number)

Sample output:
4
7
11
16
22
29
38
'''


## my solution:
from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    shuffle(number_pool)
    weekly_draw = number_pool[0:amount]
    ascending = sorted(weekly_draw)
    #sorted() function creates and RETURNS a new sorted list
    return ascending

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)


## ALTERNATIVELY:
from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    shuffle(number_pool)
    weekly_draw = number_pool[0:amount]
    weekly_draw.sort()
    #.sort() sorts the original list and returns None
    # note we cannot use ascending = weekly_draw.sort()
    # because "None" would be saved in the variable "ascending"!
    return weekly_draw

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)

####  .sort() → changes the original list, returns None.
#### sorted() → creates and returns a new sorted list.

'''
model solution provided:
from random import randint
 
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    while len(numbers) < amount:
        number = randint(lower, upper)
        if number not in numbers:
            numbers.append(number)
 
    return sorted(numbers)
'''
