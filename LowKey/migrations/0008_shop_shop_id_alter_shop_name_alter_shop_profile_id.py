# Generated by Django 4.1.1 on 2022-10-18 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LowKey', '0007_alter_shop_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.ForeignKey(default='<django.db.models.query_utils.DeferredAttribute object at 0x0000022A24DA2290>', on_delete=django.db.models.deletion.CASCADE, related_name='shop_name', to='LowKey.profile', to_field='name'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='profile_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='LowKey.profile'),
        ),
    ]
