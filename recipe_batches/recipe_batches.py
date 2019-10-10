#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # create results list with same length as recipe dictionary
    results = [0] * len(recipe.values())
    # find differences between recipe and ingredient dictionaries
    diff = set(recipe.keys()) - set(ingredients.keys())
    # add missing recipe keys to ingredients dictionary with a value of zero
    for d in diff:
        ingredients[d] = 0
    # create lists of values for recipes and ingredients
    ingredients_values = list(ingredients.values())
    recipe_values = list(recipe.values())
    # loop through results, batches is quotient of ingredient value divided by recipe value (assumes keys are in same order)
    for i in range(len(results)):
        results[i] = int(ingredients_values[i] / recipe_values[i])
    if min(results) < 1:
        return 0
    return min(results)


# def recipe_batches(recipe, ingredients):
#     # set large number for least batches
#     least = 1000000
#     # loop through keys in recipe dictionary
#     for key in recipe:
#         # check if the key from recipe exists in ingredients dictionary
#         if key in ingredients:
#             # if key exists, get quotient of ingredient amt divided by recipe amt
#             batches = ingredients[key] // recipe[key]
#             # if quotient is less than the least batch number so far, set least to quotient
#             if batches < least:
#                 least = batches
#         else:
#             return 0
#     return least


print(recipe_batches({'milk': 100, 'butter': 5, 'flour': 4, 'salt': 10}, {
      'milk': 1288, 'flour': 9, 'sugar': 95, 'butter': 9}))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 98, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
