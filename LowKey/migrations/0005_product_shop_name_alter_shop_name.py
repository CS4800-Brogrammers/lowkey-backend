# Generated by Django 4.1.1 on 2022-12-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0004_product_image_shop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
