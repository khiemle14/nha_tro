# Generated by Django 3.1.3 on 2020-12-08 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_roomimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RoomImages',
            new_name='RoomImage',
        ),
    ]
