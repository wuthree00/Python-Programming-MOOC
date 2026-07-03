## there are 3 parts to this exercise ##

# NB: Some exercises have multiple parts, and you can receive points for the different parts separately.
# You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests.

# This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used.
# The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines.
# The first line has the name of the recipe,
# the second line contains an integer number representing the preparation time in minutes,
# and the remaining line or lines contain the ingredients used, one on each line.
# The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file.
# So, there can be more than one recipe in a single file, like in the example below.

# Pancakes
# 15
# milk
# eggs
# flour
# sugar
# salt
# butter

# Meatballs
# 45
# mince
# eggs
# breadcrumbs

# Tofu rolls
# 30
# tofu
# rice
# water
# carrot
# cucumber
# avocado
# wasabi

# Cake pops
# 60
# milk
# bicarbonate
# eggs
# salt
# sugar
# cardamom
# butter

# Hint: it might be best to first read through all the lines in the file and pop them into a list,
# which is then easier to manipulate in the way described in the exercise.


### Part 1: Search for recipes based on the name of the recipe
## Please write a function named search_by_name(filename: str, word: str),
## which takes a filename and a search string as its arguments.
## The function should go through the file and select all recipes whose name contains the given search string.
## The names of these recipes are then returned in a list.

# An example of the function in action:
# found_recipes = search_by_name("recipes1.txt", "cake")

# for recipe in found_recipes:
#     print(recipe)

# Sample output:
# Pancakes
# Cake pops

# As you can see in the example above, the case of the letters is irrelevant.
# The search term cake returns both Pancakes and Cake pops, even though the latter is capitalized.

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors,
# take a look at these instructions.


## My solution:
def search_by_name(filename: str, word: str):
    with open(filename) as new_file:
        lines = [] #to store all the lines from txt files
        for line in new_file:
            lines.append(line.strip()) #append the cleaned up lines to list
        name_inside = [] #to store names of recipes that match the search word
        for i in range(len(lines)):
            if i == 0 or lines[i-1] == "": #if index is 0 (aka first line) or the previous line is blank, then the current line is the recipe name
                recipe_name = lines[i]
                if word.lower() in recipe_name.lower(): #if search word is in the recipe name
                    name_inside.append(recipe_name) #append recipe name to list if it contains the search word
        return name_inside

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
