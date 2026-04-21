## Please write a function named dict_of_numbers(), which returns a new dictionary.
## The dictionary should have the numbers from 0 to 99 as its keys.
## The value attached to each key should be the number spelled out in words.

## Please have a look at the example below:
#-----------------------------#
# numbers = dict_of_numbers() #
# print(numbers[2])           #
# print(numbers[11])          #
# print(numbers[45])          #
# print(numbers[99])          #
# print(numbers[0])           #
#-----------------------------#

# Sample output:
# two
# eleven
# forty-five
# ninety-nine
# zero

# NB: Pls dont formulate each spelled out number by hand.
# Figure out how to use loops and dictionaries in your solution.


## My solution:
def dict_of_numbers(): #dictofnumbers[number] = numberspeltout
    dictionary_of_numbers = {}
    
    #create 2 separate dictionaries for 0-19 and the tens
    zero_to_nineteen = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

    for number in range(100):
        if number < 20: #for 0-19
            dictionary_of_numbers[number] = zero_to_nineteen[number]
        elif number % 10 == 0: #for multiples of 10 (20-90)
            dictionary_of_numbers[number] = tens[number] 
        elif 20 < number < 100 and number % 10 != 0: #for numbers 21-99 that are NOT multiples of 10
            ones = number % 10 #the modulo (remainder) aft dividing by 10 is the ones place (it'd be one of the 1 to 9 keys in zero_to_nineteen)
            dictionary_of_numbers[number] = tens[number//10*10] + "-" + zero_to_nineteen[ones] #number//10*10 gets the tens place, eg 45//10*10 = 40, which IS a key found in the tens dict. add this to the value of the ones place found in the zero_to_nineteen dict
    return dictionary_of_numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])



## The model solution provided:
def dict_of_numbers():
    # Helper dictionaries
    singles = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    whole_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
 
    numbers = {}
  
    # 0 - 9
    for i in range(10):
        numbers[i] = singles[i]

    # 10 - 19 are special cases
    numbers[10] = "ten"
    numbers[11] = "eleven"
    numbers[12] = "twelve"
    numbers[13] = "thirteen"
    numbers[14] = "fourteen"
    numbers[15] = "fifteen"
    numbers[16] = "sixteen"
    numbers[17] = "seventeen"
    numbers[18] = "eighteen"
    numbers[19] = "nineteen"

    # 20 - 99
    for i in range(2, 10):
        numbers[i * 10] = whole_tens[i]
        for j in range(1, 10):
            numbers[i * 10 + j] = whole_tens[i] + "-" + singles[j]
    return numbers

if __name__ == "__main__":
    print(dict_of_numbers())
