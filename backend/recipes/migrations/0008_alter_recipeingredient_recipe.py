# Generated by Django 3.2.9 on 2023-06-04 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0007_rename_quantity_recipeingredient_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe_ingredients",
                to="recipes.recipe",
            ),
        ),
    ]