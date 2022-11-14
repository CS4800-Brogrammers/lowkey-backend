# Generated by Django 4.1.1 on 2022-11-12 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LowKey', '0002_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='shop',
            constraint=models.UniqueConstraint(fields=('user', 'shop_id'), name='unique_shop_key'),
        ),
    ]