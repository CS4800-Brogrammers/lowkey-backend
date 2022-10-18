# Generated by Django 4.1.1 on 2022-10-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0004_alter_product_product_id'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='unique_product_key',
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('profile_id', 'product_id'), name='unique_product_key'),
        ),
    ]
