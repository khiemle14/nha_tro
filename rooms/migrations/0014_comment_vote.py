# Generated by Django 3.1.3 on 2020-12-25 03:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='vote',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]