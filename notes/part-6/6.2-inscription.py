## Please write a program which asks for the name of the user and then creates an "inscription" ## in a file specified by the user. Please see the example below.

# Sample output:
# Whom should I sign this to: Ada
# Where shall I save it: inscribed.txt

# The contents of the file inscribed.txt would be:
# Hi Ada, we hope you enjoy learning Python with us! Best, Mooc.fi Team

# NB: this exercise doesn't ask you to write any functions,
# so you should not place any code within an if __name__ == "__main__" block.


## My solution:
name = input("Whom should I sign this to: ")
location = input("Where shall I save it: ")

with open(location, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


## The model solution provided:
# name = input("Whom should I sign this to: ")
# filename = input("Where shall I save it: ")
 
# with open(filename, "w") as file:
#     file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
