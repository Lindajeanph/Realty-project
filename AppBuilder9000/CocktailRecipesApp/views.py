from django.shortcuts import render


def home(request):
    return render(request, 'CocktailRecipesApp/CocktailRecipes_Home.html')
