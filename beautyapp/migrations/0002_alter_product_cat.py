# Generated by Django 5.0.1 on 2024-02-02 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'makeup'), (2, 'skincare'), (3, 'hair'), (4, 'frangrance'), (5, 'bath&body'), (6, 'health & wellness')], verbose_name='category'),
        ),
    ]
