# Generated by Django 3.1.3 on 2020-12-08 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owneruser',
            name='address',
            field=models.CharField(max_length=200, verbose_name='dia chi'),
        ),
        migrations.AlterField(
            model_name='owneruser',
            name='cccd_number',
            field=models.CharField(max_length=12, verbose_name='so can cuoc'),
        ),
        migrations.AlterField(
            model_name='owneruser',
            name='is_owner',
            field=models.IntegerField(choices=[(0, 'Nguoi thue tro'), (1, 'Chu nha tro')], default=0, verbose_name='Ban la'),
        ),
        migrations.AlterField(
            model_name='owneruser',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='so dien thoai'),
        ),
        migrations.AlterField(
            model_name='owneruser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Da co nguoi dung ten tai khoan nay.'}, max_length=150, unique=True, verbose_name='Tai khoan'),
        ),
    ]