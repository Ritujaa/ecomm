# Generated by Django 5.0.1 on 2024-02-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0004_remove_subcategory_category_product_num_ratings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='num_reviews',
            field=models.CharField(max_length=100),
        ),
    ]
