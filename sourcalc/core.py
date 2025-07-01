from sourcalc.classes import Ingredient, IngredientKind

class Recipe():
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
