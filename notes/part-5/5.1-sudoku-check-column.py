## Please write a function named column_correct(sudoku: list, column_no: int),
## which takes a two-dimensional array representing a sudoku grid,
## and an integer referring to a single column, as its arguments.
## Columns are indexed from 0.

# The function should return True or False, depending on whether the column is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

#----------------------------------#
# sudoku = [                       #
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],   #
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],   #
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],   #
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],   #
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],   #
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],   #
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],   #
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],   #
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]    #
# ]                                #
# print(column_correct(sudoku, 0)) #
# print(column_correct(sudoku, 1)) #
#----------------------------------#
# Sample output:                   #
# False                            #
# True                             #
#----------------------------------#


## Solution:
def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no]) #add the integer value at index column_no in that row, to the list called called column
    for i in range(1,10):
        if column.count(i) > 1: #if number i (which loops from 1 to 9) appears more than once in the column list
            return False
    return True

## THE LOGIC ##
# loop thru each row in the sudoku
# for each row, take the value at index column_no, add it to the column list
# now i have a list of all 9 values in that specific column
# check if numbers 1-9 appear at most once, ignore 0 which represents a blank
# return True or False

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))
