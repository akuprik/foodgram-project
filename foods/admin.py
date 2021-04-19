from django.contrib import admin

from .models import Ingredient, Recipe, IngredientRecipe


class IngredientRecipeInLine(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientRecipeInLine, )


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
