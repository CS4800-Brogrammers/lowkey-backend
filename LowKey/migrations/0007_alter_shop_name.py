# Generated by Django 4.1.1 on 2022-10-17 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0006_shop_name_alter_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.ForeignKey(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001AF365B2260>', on_delete=django.db.models.deletion.CASCADE, related_name='shop_name', to='LowKey.profile', to_field='name'),
        ),
    ]