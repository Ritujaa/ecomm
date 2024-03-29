# Generated by Django 5.0.1 on 2024-02-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0006_product_pdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='item_form',
            field=models.CharField(choices=[('Gel', 'Gel'), ('Cream', 'Cream'), ('Lotion', 'Lotion')], default='Gel', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='net_quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='number_of_items',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='skin_type',
            field=models.CharField(choices=[('All', 'All'), ('Oily', 'Oily'), ('Combination', 'Combination')], default='all', max_length=50),
        ),
    ]
