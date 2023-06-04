from django.shortcuts import get_object_or_404
from rest_framework import filters, status
from rest_framework.response import Response
from recipes.models import Recipe

from recipes.models import Ingredient, RecipeIngredient


def add_ingredients_to_recipe(recipe, ingredients):
    for ingredient_data in ingredients:
        amount = ingredient_data["amount"]
        ingredient = Ingredient.objects.get(id=ingredient_data["id"])
        RecipeIngredient.objects.create(
            recipe=recipe,
            ingredient=ingredient,
            amount=amount,
        )


class RecipeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        is_in_shopping_cart = request.query_params.get("is_in_shopping_cart")
        is_favorited = request.query_params.get("is_favorited")
        author = request.query_params.get("author")
        tags = request.query_params.getlist("tags")

        if is_in_shopping_cart == "1":
            queryset = queryset.filter(shopping_cart__user=request.user)
        if is_favorited == "1":
            queryset = queryset.filter(favorites__user=request.user)
        if author:
            queryset = queryset.filter(author__id=author)
        if tags:
            return queryset.filter(tags__slug__in=tags).distinct()

        return queryset

def process_recipe_saving(request, pk, serializer, model):
    recipe = get_object_or_404(Recipe, id=pk)
    if request.method == "POST":
        serializer = serializer(data={
            "recipe": recipe.id,
            "user": request.user.id,
        }, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    model.objects.filter(recipe=recipe, user=request.user).delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
