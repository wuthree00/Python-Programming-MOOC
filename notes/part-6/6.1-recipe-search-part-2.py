## there are 3 parts to this exercise ##

## Part 1[https://github.com/wuthree00/Python-Programming-MOOC/blob/main/notes/part-6/6.1-recipe-search-part-1.py]

### Part 2: Search for recipes based on the preparation time
## Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments.
## The function should go through the file and select all recipes whose preparation time is at most the number given.

# The names of these recipes are again returned in a list,
# but the preparation time should be appended to each name.
# Please have a look at the example below.

# found_recipes = search_by_time("recipes1.txt", 20)

# for recipe in found_recipes:
#     print(recipe)

# Sample output
# Pancakes, preparation time 15 min

## My solution:
def search_by_time(filename: str, prep_time: int):
    with open(filename) as new_file:
        lines = [] #to store all the lines from txt files
        for line in new_file:
            lines.append(line.strip())
        name_and_time = [] #to store recipes & time taken that take as long or less than prep_time
        for i in range(len(lines)):
            if i == 0 or lines[i-1] == "":
                recipe_name = lines[i]
                recipe_time = int(lines[i+1])
                if recipe_time <= prep_time:
                    the_recipe = f"{recipe_name}, preparation time {recipe_time} min"
                    name_and_time.append(the_recipe)
        return name_and_time
                    
if __name__ == "__main__":
    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)


