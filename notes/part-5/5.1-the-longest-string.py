## Please write a function named longest(strings: list), which takes a list of strings as its argument.
## The function finds and returns the longest string in the list.
## You may assume there is always a single longest string in the list.

#------------------------------------------------------------------
# An example of expected behaviour:
# if __name__ == "__main__":
#     strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
#     print(longest(strings))

## Sample output
# howdydoody
#------------------------------------------------------------------


## Solution:
def longest(strings: list):
    da_longest = ""
    for string in strings:
        if len(string) > len(da_longest):
            da_longest = string
    return da_longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
