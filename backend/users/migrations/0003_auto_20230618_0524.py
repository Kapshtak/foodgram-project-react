# Generated by Django 3.2.9 on 2023-06-18 05:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_subscription_options_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscription",
            options={
                "verbose_name": "подписка",
                "verbose_name_plural": "подписки",
            },
        ),
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("email",),
                "verbose_name": "пользователь",
                "verbose_name_plural": "пользователи",
            },
        ),
        migrations.AlterField(
            model_name="subscription",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follower",
                to=settings.AUTH_USER_MODEL,
                verbose_name="автор",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
                verbose_name="подписчик",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="электронная почта"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="имя"),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=150, verbose_name="фамилия"),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=150, verbose_name="пароль"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                max_length=150, unique=True, verbose_name="юзернейм"
            ),
        ),
    ]
