# Generated by Django 4.2.1 on 2023-06-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.PositiveIntegerField(help_text="in minutes"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]