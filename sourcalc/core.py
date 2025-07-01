from sourcalc.classes import Ingredient, IngredientKind

class Recipe():
    def __init__(self):
        self.ingredients = []
        self.innoculation = 1.0
        self.hydration = 1.0
        self.n_loaves = 1
        self.basket_capacity = 100

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
