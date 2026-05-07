from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'cooking_time', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Classic Spaghetti Bolognese',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Briefly describe your recipe...',
            }),
            'ingredients': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': '2 cups flour\n1 tsp salt\n3 eggs\n...',
            }),
            'instructions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Step 1: Preheat oven to 180°C\nStep 2: Mix ingredients...',
            }),
            'cooking_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 30',
                'min': 1,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }
        labels = {
            'cooking_time': 'Cooking Time (minutes)',
            'image': 'Recipe Photo (optional)',
        }
        help_texts = {
            'ingredients': 'Enter each ingredient on a separate line.',
            'instructions': 'Enter each step on a separate line.',
        }
