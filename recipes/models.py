from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    ingredients = models.TextField(help_text="List each ingredient on a new line")
    instructions = models.TextField(help_text="Step-by-step cooking instructions")
    cooking_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})

    def get_ingredients_list(self):
        """Return ingredients as a list of lines."""
        return [line.strip() for line in self.ingredients.splitlines() if line.strip()]

    def get_instructions_list(self):
        """Return instructions as a numbered list."""
        return [line.strip() for line in self.instructions.splitlines() if line.strip()]
