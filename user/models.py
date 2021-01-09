from django.contrib.auth.models import AbstractUser
from django.db import models



class UserType(models.IntegerChoices):
    RENTER = 0, 'Người thuê trọ'
    OWNER = 1, 'Chủ nhà trọ'


class OwnerUser(AbstractUser):
    full_name = models.CharField(
        'Ho va ten',
        max_length=120,
        help_text=(''),
        blank=False,
        default='',
    )
    username = models.CharField(
        ('Tai khoan'),
        max_length=150,
        unique=True,
        help_text=(''),
        # validators=[username_validator],
        error_messages={
            'unique': ("Da co nguoi dung ten tai khoan nay."),
        },
    )
    is_owner = models.IntegerField(

        'Ban la',
        choices=UserType.choices,
        default=0,

    )
    address = models.CharField(
        'dia chi',
        max_length=200,

    )
    phone_number = models.CharField(
        'so dien thoai',
        max_length=11,
        unique=False,
    )
    cccd_number = models.CharField(
        'so can cuoc',
        max_length=12,
        unique=False,
    )
    is_active = models.BooleanField(default=True, )
    can_edit_profile = models.BooleanField(default=False, )
    avatar = models.ImageField(blank=True)


