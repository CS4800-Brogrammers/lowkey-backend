# Generated by Django 4.1.1 on 2022-11-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0004_alter_product_rating_alter_shop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='profile_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.TextField(),
        ),
    ]
