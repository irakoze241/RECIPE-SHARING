from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Recipe
from .forms import RecipeForm


def home(request):
    """Home page — show all recipes with optional search."""
    query = request.GET.get('q', '').strip()
    recipes = Recipe.objects.select_related('author').all()

    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'recipes': recipes,
        'query': query,
        'total_count': Recipe.objects.count(),
    }
    return render(request, 'recipes/home.html', context)


def recipe_detail(request, pk):
    """Full detail page for a single recipe."""
    recipe = get_object_or_404(Recipe.objects.select_related('author'), pk=pk)
    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_detail.html', context)


@login_required
def recipe_create(request):
    """Create a new recipe."""
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, f'🎉 Recipe "{recipe.title}" created successfully!')
            return redirect('recipe-detail', pk=recipe.pk)
    else:
        form = RecipeForm()

    context = {'form': form, 'action': 'Create'}
    return render(request, 'recipes/recipe_form.html', context)


@login_required
def recipe_update(request, pk):
    """Edit an existing recipe — only the author can edit."""
    recipe = get_object_or_404(Recipe, pk=pk)

    if recipe.author != request.user:
        messages.error(request, 'You are not allowed to edit this recipe.')
        return redirect('recipe-detail', pk=recipe.pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Recipe "{recipe.title}" updated successfully!')
            return redirect('recipe-detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    context = {'form': form, 'action': 'Update', 'recipe': recipe}
    return render(request, 'recipes/recipe_form.html', context)


@login_required
def recipe_delete(request, pk):
    """Delete a recipe — only the author can delete."""
    recipe = get_object_or_404(Recipe, pk=pk)

    if recipe.author != request.user:
        messages.error(request, 'You are not allowed to delete this recipe.')
        return redirect('recipe-detail', pk=recipe.pk)

    if request.method == 'POST':
        title = recipe.title
        recipe.delete()
        messages.success(request, f'🗑️ Recipe "{title}" has been deleted.')
        return redirect('home')

    context = {'recipe': recipe}
    return render(request, 'recipes/recipe_confirm_delete.html', context)


@login_required
def my_recipes(request):
    """Dashboard — recipes created by the logged-in user."""
    recipes = Recipe.objects.filter(author=request.user).order_by('-created_at')
    context = {'recipes': recipes}
    return render(request, 'recipes/my_recipes.html', context)
