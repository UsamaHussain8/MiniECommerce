# Generated by Django 4.1.7 on 2023-08-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
