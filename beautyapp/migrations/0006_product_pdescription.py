# Generated by Django 5.0.1 on 2024-02-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0005_alter_product_num_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdescription',
            field=models.TextField(blank=True, null=True),
        ),
    ]