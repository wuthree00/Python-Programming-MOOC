## The file fruits.csv contains names of fruits, and their prices,
## in the format specified in this example:

# banana;6.50
# apple;4.95
# orange;8.0
# ...etc...

# Please write a function named read_fruits,
# which reads the file and returns a dictionary based on the contents.
# In the dictionary, the name of the fruit should be the key,
# and the value should be its price. Prices should be of type float.

# NB: the function does not take any arguments.
# The file you are working with is always named fruits.csv.


## Solution:
def read_fruits():
    with open("fruits.csv") as new_file:
        #dictionary[name] = price
        fruit = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])
            fruit[name] = price
        return fruit

def main():
    fruit = read_fruits()
    print(fruit)

if __name__ == "__main__":
    main()


##### NOTE: usually i use #####
#-----------------------------#
# if __name__ == "__main__":  #
#    print(read_fruits())     #
#-----------------------------#


# BUT
# → its cleaner to put what i want the code to do in the main() function,
# so that i can simply call main(),
# which then runs the code inside – which is to:

# 1) execute the read_fruits() function
# 2) save the return value of read_fruits() in the ‘fruit’ variable, and
# 3) print it out

## TLDR how to use main():
# Put whatever I want the exercise to do in main(),
# so that I can simply test main() by calling it in a simple line,
# instead of writing multiple lines under *if __name__ == "__main__":*


## The model solution provided:
# def read_fruits():
#     with open("fruits.csv") as file:
#         fruits = {}
#         for row in file:
            # split to two pieces
#             data = row.split(";")
#             # name first, price second
            fruits[data[0]] = float(data[1])
#     return fruits
