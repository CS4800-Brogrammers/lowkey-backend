# Generated by Django 4.1.1 on 2022-11-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0002_shop_email_shop_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]