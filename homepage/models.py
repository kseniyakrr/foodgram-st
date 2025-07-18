from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ingredient(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        null=False, 
        blank=False, 
        verbose_name="Название ингредиента", 
        help_text="Название ингредиента"
    )
    
    unit = models.CharField(
        max_length=20, 
        null=False,
        blank=False,
        verbose_name="Единица измерения",
        help_text="Единица измерения",
        default="г"
    )

    def __str__(self):
        return f"{self.name} ({self.unit})"
    

class Recipe(models.Model):
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    
    name = models.CharField(
        max_length=128, 
        null=False, 
        blank=False, 
        verbose_name="Название рецепта"
    )
    
    image = models.ImageField(
        upload_to='recipes/images/',
        null=False, 
        blank=False, 
        verbose_name="Картинка рецепта"
    )
    
    text = models.TextField(
        max_length=1024, 
        null=False, 
        blank=False, 
        verbose_name="Описание рецепта"
    )
    
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        blank=False, 
        verbose_name="Ингредиенты", 
        related_name="recipes"
    )
    
    cooking_time = models.PositiveIntegerField(
        null=False, 
        blank=False, 
        verbose_name="Время приготовления (в минутах)"
    )

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        verbose_name="Ингредиент"
    )
    
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        verbose_name="Рецепт"
    )
    
    amount = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        verbose_name="Количество"
    )

    class Meta:
        unique_together = [['recipe', 'ingredient']]
        verbose_name = "Ингредиент рецепта"
        verbose_name_plural = "Ингредиенты рецептов"

    def __str__(self):
        return f"{self.amount} {self.ingredient.unit} {self.ingredient.name} для {self.recipe.name}"