from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect

from rooms.models import Room, RoomImage
from .forms import ImageForm, RoomCreateForm


# Create your views here.
@login_required
def post(request):
    if not request.user.is_owner:
        return redirect('home')
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        form = RoomCreateForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')

        if form.is_valid():
            owner = request.user
            data = form.cleaned_data
            new_room = Room.objects.create(
                owner=owner,
                title=data['title'],
                price=data['price']
                , area=data['area']
                , address=data['address']
                , nearby='abc'
                , type=data['type']
                , chung_chu=False
                , private_bathroom=data['private_bathroom']
                , co_nonglanh=data['co_nonglanh']
                , kitchen=data['kitchen']
                , air_conditional=data['air_conditional']
                , ban_cong=data['ban_cong']
                , service_charge=data['service_charge']
                , other_ultily=data['other_ultily']
                , longevity=data['longevity']
            )
            print("abcde")
            for file in files:
                RoomImage.objects.create(
                    room=new_room,
                    images=file
                )
            return redirect('/profile/')

    return render(request, 'post.html')
