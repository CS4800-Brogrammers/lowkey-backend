# Generated by Django 4.1.1 on 2022-10-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0003_alter_product_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]