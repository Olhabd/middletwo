from django.test import TestCase
from django.utils import timezone

from .models import Category, Recipe

# Create your tests here.

class CategoryModelTest(TestCase):

    def test_category_str_returns_name(self):

        category = Category.objects.create(name="Desserts")

        self.assertEqual(str(category), "Desserts")


class RecipeModelTest(TestCase):

    def test_recipe_str_returns_title(self):

        category = Category.objects.create(name="Main dishes")

        recipe = Recipe.objects.create(
            title = "Pasta",
            description = "Simple pasta recipe",
            instructions = "Boil pasta and add sauce.",
            ingredients = "Pasta, sauce, cheese",
            created_at = timezone.now(),
            updated_at = timezone.now(),
            category = category,
        )

        self.assertEqual(str(recipe), "Pasta")

    def test_recipe_belongs_to_category(self):

        category = Category.objects.create(name="Breakfast")

        recipe = Recipe.objects.create(
            title = "Omelette",
            description = "Egg recipe",
            instructions = "Fry eggs.",
            ingredients = "Eggs, salt",
            created_at = timezone.now(),
            updated_at = timezone.now(),
            category = category,
        )

        self.assertEqual(recipe.category, category)
