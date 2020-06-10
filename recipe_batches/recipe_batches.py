#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # for each  recipe's ingredients, 
  # check to see if ingredients are listed in the "ingredients" dict
  # if the the ingredient is there, divide the amount from  
  # not sure what this is for yet
  minimum_in = 0

  # set as comparable value
  max_batches = 100000000

  available_ingredients = None

  recipe_values = []
  recipe_values = [recipe.values()]

  #if recipe ingredients is > ingredients, 0 batches avail
  if len(recipe) > len(ingredients):
    max_batches = 0

  # or else, going through the recipe, if the recipe_ingredient is > the 
  # ingredient avail in the ingredient dictionary, 
  # divide the ingredient amount into the avail amount and round down. 
  # the smallest number from the recipe ingredient list returned, is the batch available.


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))