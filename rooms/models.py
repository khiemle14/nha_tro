from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from user.models import OwnerUser
from multiupload.fields import MultiFileField, MultiMediaField


# Create your models here.
class RoomType(models.Model):
    name = models.CharField(max_length=150, default='')
    amount_of_room_intype = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class KitchenChoice(models.IntegerChoices):
    PRIVATE = 0, 'Bếp riêng'
    PUBLIC = 1, 'Chung'
    UNABLE = 2, 'Không nấu ăn'


class Room(models.Model):
    owner = models.ForeignKey(OwnerUser, on_delete=models.CASCADE, default=5)

    title = models.CharField('Tieu de', max_length=150, blank=True)

    # These attitude are showed on top of post
    price = models.IntegerField('Gia phong', )
    area = models.IntegerField('Dien tich phong', )

    address = models.CharField('Dia chi', max_length=150, )
    nearby = models.TextField('Gan cac dia diem', max_length=300, )

    # Information of room
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE, )

    chung_chu = models.BooleanField(default=False)
    private_bathroom = models.BooleanField('Nha ve sinh rieng', )
    co_nonglanh = models.BooleanField('Co nong lanh', )
    kitchen = models.IntegerField(
        choices=KitchenChoice.choices,
        default=0,
    )
    air_conditional = models.BooleanField('Dieu hoa')
    ban_cong = models.BooleanField('Ban cong')
    service_charge = models.TextField('Gia dich vu', max_length=100)
    other_ultily = models.TextField('Cac tien ich khac')
    update_at = models.DateTimeField(auto_now=True)

    # number of dates that post in active mode
    longevity = models.PositiveBigIntegerField(validators=[MinValueValidator(7), MaxValueValidator(364)])

    # only admin can change value of this variable
    is_active = models.BooleanField(default=False)
    is_rented = models.BooleanField(default=False)
    pro_city_id = models.IntegerField(blank=True, default=1)
    pro_city_pa_id = models.IntegerField(blank=True, default=2)

    viewed = models.IntegerField(default=24, )

    def __str__(self):
        return 'room ' + self.title


class RoomImage(models.Model):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE, )
    images = models.FileField(upload_to='media/images/rooms/')


class Comment(models.Model):
    comment_user = models.ForeignKey(OwnerUser, on_delete=models.CASCADE, )
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField(max_length=350)
    vote = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_user.full_name + self.comment


class Report(models.Model):
    report_user = models.ForeignKey(OwnerUser, on_delete=models.CASCADE, )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, )
    reason = models.TextField(max_length=350)


class CaredRoom(models.Model):
    user_id = models.ForeignKey(OwnerUser, on_delete=models.CASCADE, )
    room = models.ForeignKey(Room, on_delete=models.CASCADE, )
