# Generated by Django 3.1.3 on 2020-12-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_room_is_rented'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='chung_chu',
            field=models.BooleanField(default=False),
        ),
    ]
