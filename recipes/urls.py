from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipes/create/', views.recipe_create, name='recipe-create'),
    path('recipes/<int:pk>/edit/', views.recipe_update, name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='recipe-delete'),
    path('my-recipes/', views.my_recipes, name='my-recipes'),
]
