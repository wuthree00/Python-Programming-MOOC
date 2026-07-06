## there are 3 parts to this exercise ##

## Part 1[https://github.com/wuthree00/Python-Programming-MOOC/blob/main/notes/part-6/6.1-recipe-search-part-1.py]
## Part 2[https://github.com/wuthree00/Python-Programming-MOOC/blob/main/notes/part-6/6.1-recipe-search-part-2.py]

### Part 3: Search for recipes based on the ingredients
## A word of caution: this third part of the exercise is considerably more demanding than the previous two.
# If you feel like you aren't making headway, it may be worth your while to move on,
# complete the other exercises in this part of the material,
# and then come back to this exercise if you have time later.
# Remember, you can submit and receive points for the first two parts of this exercise even if you haven't completed the third part.

## Please write a function named search_by_ingredient(filename: str, ingredient: str),
## which takes a filename and a search string as its arguments.
## The function should go through the file and select all recipes whose ingredients contain the given search string.

# The names of these recipes are returned in a list just like in the second part,
# with the preparation time appended. Please have a look at the example below.

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)

# Sample output:
# Pancakes, preparation time 15 min
# Meatballs, preparation time 45 min
# Cake pops, preparation time 60 min


## My solution:
def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as new_file:
        lines = [] #to store all the lines from txt files
        for line in new_file:
            lines.append(line.strip())
        name_and_ingredient = [] #to store recipes w that ingredient
        for i in range(len(lines)):
            if i == 0 or lines[i-1] == "": #if its the first recipe name or previous line is blank (aka current index is a recipe name)
                recipe_name = lines[i]
                recipe_time = int(lines[i+1])

                for j in range(i+2, len(lines)): #start checking the ingredients from the line AFTER recipe time
                    if lines[j] == "": #if current line is blank, break out of loop since this marks the END of that recipe's ingredients list
                        break
                        
                    if ingredient.lower() == lines[j].lower():
                        recipe = f"{recipe_name}, preparation time {recipe_time} min"
                        name_and_ingredient.append(recipe)
                        break #stop checking this recipe once ingredient has been found
        return name_and_ingredient

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "milk")
    for recipe in found_recipes:
        print(recipe)


## The model solution provided:
# def read_file(filename):
#     with open(filename) as file:
#         rows = []
#         for row in file:
#             rows.append(row.strip())
 
#     recipes = []
#     name_in_row = True
#     prep_time_in_row = True
#     new = { "ingredients": []}
#     for row in rows:
#         if name_in_row:
#             new["name"] = row
#             name_in_row = False
#             prep_time_in_row = True
#         elif prep_time_in_row:
#             new["prep_time"] = int(row)
#             prep_time_in_row = False
#         elif len(row) > 0:
#             new["ingredients"].append(row)
#         else:
#             recipes.append(new)
#             name_in_row = True
#             new = {"ingredients": []}
#     recipes.append(new)
 
#     return recipes
 
# def search_by_name(filename: str, word: str):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if word.lower() in recipe["name"].lower():
#             found.append(recipe["name"])
 
#     return found
 
# def search_by_time(filename: str, time: int):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if recipe["prep_time"] <= time:
#             found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
#     return found
 
# def search_by_ingredient(filename: str, ingredient: str):
#     recipes = read_file(filename)
 
#     found = []
#     for recipe in recipes:
#         if ingredient.lower() in recipe["ingredients"]:
#             found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
#     return found
