## This is the very last sudoku task.
## This time we will create a slightly different version of the function for adding new numbers to the grid.

## The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid,
## two integers referring to the row and column indexes of a single square,
## and a single digit between 1 and 9, as its arguments.
## The function should return a copy of the original grid with the new digit added in the correct location.
## The function should not change the original grid received as a parameter.

# The print_sudoku function from the previous exercise could be useful for testing,
# and it is used in the example below:

#-------------------------------------------#
# sudoku  = [                               #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],          #
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]           #
# ]                                         #
#                                           #
# grid_copy = copy_and_add(sudoku, 0, 0, 2) #
# print("Original:")                        #
# print_sudoku(sudoku)                      #
# print()                                   #
# print("Copy:")                            #
# print_sudoku(grid_copy)                   #
#-------------------------------------------#

## Sample output
#-------------------#
#Original:          #
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#                   #
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#                   #
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#                   #
#Copy:              #
#2 _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#                   #
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#                   #
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#_ _ _  _ _ _  _ _ _#
#-------------------#


# Hint When dealing with nested lists you should be extra careful when copying.
# What all needs to be explicitly copied, and where do changes actually have an effect?
# The visualisation tool is a great help here, too,
# although the size of the sudoku grid will make the view less orderly than usual.


## Solution:
def print_sudoku(sudoku: list):
    for i in range(9): #loop thru 0 to 8 (9 rows)
        if i % 3 == 0 and i != 0: #for every 3rd & 6th row, print a blank line
            print()

        for j in range(9): #loop thru 0-8 (9 squares aka columns)
            if sudoku[i][j] > 0: #if that running number > 0, print that no. + space
                print(f"{sudoku[i][j]}", end=" ")
            else: #if that running number is 0, print _ + space
                print("_", end=" ")
            if j == 2 or j == 5: #after column of index 2 & 5 (aft 3rd & 6th square), print a space to separate the 3 _)
                print(" ", end="") #print a space without printing new line
        print() #print a new line after printing each row

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    #to create a copy of the sudoku grid, first create an empty list for that copy
    sudoku_copy = []
    for row in sudoku:
        sudoku_copy.append(row[:]) #this appends a copy of each row (using slicing) to sudoku_copy list
    #now, modify the COPY of the sudoku grid by adding each no. to the specified row&column
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)


## The model solution provided:
# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#     new_list = []
#     for r in sudoku:
#         new_list.append(r[:])
 
#     new_list[row_no][column_no] = number
#     return new_list
