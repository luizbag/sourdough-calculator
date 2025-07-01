from sourcalc.core import Recipe
from sourcalc.classes import Ingredient, IngredientKind

class TestRecipe:
    def test_init_recipe(self):
        recipe = Recipe()
        assert len(recipe.ingredients)==0
    
    def test_add_ingredient(self):
        recipe = Recipe()
        ingredient = Ingredient("Wheat Flour", 1, IngredientKind.Flour)
        recipe.add_ingredient(ingredient)
        assert len(recipe.ingredients)==1
