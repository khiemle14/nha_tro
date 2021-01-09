# Generated by Django 3.1.3 on 2020-12-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20201222_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='address',
            field=models.CharField(max_length=150, verbose_name='Dia chi'),
        ),
        migrations.AlterField(
            model_name='room',
            name='air_conditional',
            field=models.BooleanField(verbose_name='Dieu hoa'),
        ),
        migrations.AlterField(
            model_name='room',
            name='area',
            field=models.IntegerField(verbose_name='Dien tich phong'),
        ),
        migrations.AlterField(
            model_name='room',
            name='ban_cong',
            field=models.BooleanField(verbose_name='Ban cong'),
        ),
        migrations.AlterField(
            model_name='room',
            name='co_nonglanh',
            field=models.BooleanField(verbose_name='Co nong lanh'),
        ),
        migrations.AlterField(
            model_name='room',
            name='kitchen',
            field=models.IntegerField(verbose_name='Phong bep'),
        ),
        migrations.AlterField(
            model_name='room',
            name='nearby',
            field=models.TextField(max_length=300, verbose_name='Gan cac dia diem'),
        ),
        migrations.AlterField(
            model_name='room',
            name='other_ultily',
            field=models.TextField(verbose_name='Cac tien ich khac'),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(verbose_name='Gia phong'),
        ),
        migrations.AlterField(
            model_name='room',
            name='private_bathroom',
            field=models.BooleanField(verbose_name='Nha ve sinh rieng'),
        ),
        migrations.AlterField(
            model_name='room',
            name='service_charge',
            field=models.TextField(max_length=100, verbose_name='Gia dich vu'),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Tieu de'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='amount_of_room_intype',
            field=models.IntegerField(default=0),
        ),
    ]
