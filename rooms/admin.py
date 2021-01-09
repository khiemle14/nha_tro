from django.contrib import admin
from .models import Room, RoomImage, RoomType, Comment, Report, CaredRoom


# Register your models here.

class RoomImageAdmin(admin.StackedInline):
    model = RoomImage


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageAdmin]

    class Meta:
        model = Room


@admin.register(RoomImage)
class RoomImageAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass


@admin.register(CaredRoom)
class CaredRoomAdmin(admin.ModelAdmin):
    pass
