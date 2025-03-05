# Generated by Django 5.1.6 on 2025-03-05 06:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='ratings',
            field=models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
