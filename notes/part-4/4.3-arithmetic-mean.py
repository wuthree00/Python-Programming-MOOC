## Please write a function named mean, which takes a list of integers as an argument.
## The function returns the arithmetic mean of the values in the list.

## Sample input:
# my_list = [1, 2, 3, 4, 5]
# result = mean(my_list))
# print("mean value is", result)

## Sample output
# mean value is 3.0


## Solution:
def mean(my_list):
    total = sum(my_list)
    average = total / len(my_list)
    return average  #this makes sure the mean is printed out

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)
