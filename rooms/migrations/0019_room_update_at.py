# Generated by Django 3.1.3 on 2020-12-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0018_room_chung_chu'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
