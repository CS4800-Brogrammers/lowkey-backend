# Generated by Django 4.1.1 on 2022-10-25 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=2, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.TextField(default='Brogrammers', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.ForeignKey(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001B96FFFC6A0>', on_delete=django.db.models.deletion.CASCADE, related_name='shop_name', to='LowKey.profile', to_field='name'),
        ),
    ]
