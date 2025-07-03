from sourcalc.core import Recipe
from sourcalc.dataclasses import Ingredient, IngredientKind

class TestRecipe:
    def test_init_recipe(self):
        recipe = Recipe()
        assert recipe.innoculation == 1.0
        assert recipe.hydration == 1.0
        assert recipe.n_loaves == 1
        assert recipe.basket_capacity == 100
        assert len(recipe.ingredients) == 0
    
    def test_add_ingredient(self):
        recipe = Recipe()
        ingredient = Ingredient("Wheat Flour", 1, IngredientKind.Flour)
        recipe.add_ingredient(ingredient)
        assert len(recipe.ingredients) == 1

    def test_remove_ingredient(self):
        recipe = Recipe()
        ingredient = Ingredient("Wheat Flour", 1, IngredientKind.Flour)
        recipe.add_ingredient(ingredient)
        assert len(recipe.ingredients) == 1
        recipe.remove_ingredient(ingredient)
        assert len(recipe.ingredients) == 0
