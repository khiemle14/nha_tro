from django.forms import ModelForm
from rooms.models import Room, RoomImage


class RoomCreateForm(ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'price', 'area', 'address',  'type', 'private_bathroom', 'co_nonglanh',
                  'kitchen', 'air_conditional', 'ban_cong', 'service_charge', 'other_ultily', 'longevity','pro_city_pa_id', 'pro_city_id']
        labels = {
            'type': 'Loai',
        }


class ImageForm(ModelForm):
    class Meta:
        model = RoomImage
        fields = ['images', ]


class PostForm(ModelForm):
    class Meta:
        fields = RoomCreateForm.Meta.fields + ['images', ]
