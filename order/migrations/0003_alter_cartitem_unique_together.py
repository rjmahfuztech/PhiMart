# Generated by Django 5.1.6 on 2025-02-27 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_cart_id'),
        ('product', '0003_review'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart', 'product')},
        ),
    ]
