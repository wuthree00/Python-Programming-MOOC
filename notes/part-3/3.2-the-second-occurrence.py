## Please write a program which finds the second occurrence of a substring.
## If there is no second (or first) occurrence, the program should print out a message accordingly.

# In this exercise the occurrences cannot overlap.
# For example, in the string aaaa the second occurrence of the substring aa is at index 2.

# Some examples of expected behaviour:

## Sample output
# Please type in a string: abcabc
# Please type in a substring: ab
# The second occurrence of the substring is at index 3.

## Sample output
# Please type in a string: methodology
# Please type in a substring: o
# The second occurrence of the substring is at index 6.

## Sample output
# Please type in a string: aybabtu
# Please type in a substring: ba
# The substring does not occur twice in the string.


## Solution
string = input("Please type in a string:")
substring = input("Please type in a substring:")
first_appearance = string.find(substring) #this is the index where substring first appears (INTEGER)

if first_appearance == -1:
    print("The substring does not occur twice in the string.")

#the next substring must appear after the first one FULLY ends (aka after the length of the first entire substring)
else:
    second_appearance = string.find(substring, first_appearance+len(substring))
    if second_appearance == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_appearance}.")
