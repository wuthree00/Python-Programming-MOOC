## Please write a function named row_correct(sudoku: list, row_no: int),
## which takes a two-dimensional array representing a sudoku grid,
## and an integer referring to a single row, as its arguments.
## Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly,
# that is, whether it contains each of the numbers 1 to 9 at most once.

#--------------------------------#
# sudoku = [                     #
#   [9, 0, 0, 0, 8, 0, 3, 0, 0], #
#   [2, 0, 0, 2, 5, 0, 7, 0, 0], #
#   [0, 2, 0, 3, 0, 0, 0, 0, 4], #
#   [2, 9, 4, 0, 0, 0, 0, 0, 0], #
#   [0, 0, 0, 7, 3, 0, 5, 6, 0], #
#   [7, 0, 5, 0, 6, 0, 4, 0, 0], #
#   [0, 0, 7, 8, 0, 3, 9, 0, 0], #
#   [0, 0, 1, 0, 0, 0, 0, 0, 3], #
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]  #
# ]                              #
#                                #
# print(row_correct(sudoku, 0))  #
# print(row_correct(sudoku, 1))  #
#--------------------------------#
# Sample output:                 #
# True                           #
# False                          #
#--------------------------------#


## Solution:
def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no] #this sets each row to be referenced by the row number
    for i in range(1,10): #this means 'let i be each number from 1 to 9, one at a time'
        if row.count(i) > 1: #this means 'if number i appears more than once in this row'
            return False
    return True

#note: i dont need the row_correct() function to loop through each row in the entire sudoku, because the function is only supposed to check for the row that is being called out in the argument ‘row_no’

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

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
