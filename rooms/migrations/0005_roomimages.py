# Generated by Django 3.1.3 on 2020-12-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_remove_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/rooms')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
            ],
        ),
    ]