from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
import random
# Create your views here.
from django.views.generic import TemplateView, ListView

from user.models import OwnerUser
from .models import Room, Comment, Report, CaredRoom
from django.forms import ModelForm, forms


class SiteRoomView(TemplateView):
    template_name = 'room.html'

    # def get_context_data(self, **kwargs):


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['reason', ]


# def roomDetail(request, id):

def roomDetail(request, id):
    context = {}
    room_detail = Room.objects.get(id=id)
    context['room_detail'] = room_detail
    room_detail.viewed += 1
    comments = Comment.objects.filter(room=id)
    context['comments'] = comments
    id_con = id
    context['id_con'] = id_con
    room_detail.save()

    return render(request, 'thongtinphongtro.html', context)


def postedRoom(request):
    context = {}
    context['roomlist'] = Room.objects.filter(owner=request.user)
    return render(request, 'profile.html', context)


def phongtro(request):
    context = {}
    context['roomlist'] = Room.objects.filter(type=1)
    return render(request, 'roomList.html', context)


def ccmn(request):
    context = {}
    context['roomlist'] = Room.objects.filter(type=2)
    return render(request, 'roomList.html', context)


def nnc(request):
    context = {}
    context['roomlist'] = Room.objects.filter(type=3)
    return render(request, 'roomList.html', context)


def hcm(request):
    context = {}
    context['ad']='Hồ chí minh'
    context['roomlist'] = Room.objects.filter(
            Q(title__contains='Hồ') |
            Q(address__contains='Hồ')|
            Q(title__contains='chí') |
            Q(address__contains='chí')|
            Q(title__contains='minh') |
            Q(address__contains='minh')
    )
    return render(request, 'roomListse.html', context)


def hn(request):
    context = {}
    context['ad'] = 'Hà Nội'
    context['roomlist'] = Room.objects.filter(
        Q(title__contains='Hà') |
        Q(address__contains='Hà')|
        Q(title__contains='nội') |
        Q(address__contains='nội')
    )
    return render(request, 'roomListse.html', context)


def hue(request):
    context = {}
    context['ad'] = 'Thừa Thiên Huế'
    context['roomlist'] = Room.objects.filter(
        Q(title__contains='Huế') |
        Q(address__contains='Huế')
    )
    return render(request, 'roomListse.html', context)


def danang(request):
    context = {}
    context['ad'] = 'Đà nẵng'
    context['roomlist'] = Room.objects.filter(
        Q(title__contains='Đà') |
        Q(address__contains='Đà')|
        Q(title__contains='nẵng') |
        Q(address__contains='nẵng')
    )
    return render(request, 'roomListse.html', context)


def cantho(request):
    context = {}
    context['ad'] = 'Cần thơ'
    context['roomlist'] = Room.objects.filter(
        Q(title__contains='Cần thơ') |
        Q(address__contains='Cần thơ')
    )
    return render(request, 'roomListse.html', context)


def ccnc(request):
    context = {}
    context['roomlist'] = Room.objects.filter(type=4)
    return render(request, 'roomList.html', context)


def roomDetails(request):
    if request.method == 'POST':
        user = request.user
        context = {}
        if request.POST.get('comment') and request.is_ajax:
            new_comment = Comment.objects.create(
                room=Room.objects.get(id=request.POST.get('id_con')),
                comment_user=user,
                comment=request.POST.get('comment'),
                vote=random.randint(1, 5),

            )
            context['comments'] = Comment.objects.filter(room_id=request.POST.get('id_con'))
            context['id_con'] = request.POST.get('id_con')
            return render(request, 'comment_snipset.html', context)
        if request.POST.get('liked') and request.is_ajax():
            new_caredroom = CaredRoom.objects.update_or_create(
                room=Room.objects.get(id=request.POST.get('id_con')),
                user_id=user,

            )
            context['comments'] = Comment.objects.filter(room_id=request.POST.get('id_con'))
            context['id_con'] = request.POST.get('id_con')
            return render(request, 'comment_snipset.html', context)
        if request.POST.get('rented') and request.is_ajax():
            rented_room = Room.objects.get(id=request.POST.get('id_con'))
            print(rented_room.is_rented)
            rented_room.is_rented = (1 and request.POST.get('rented'))
            print(rented_room.is_rented)

            rented_room.save()

            context['comments'] = Comment.objects.filter(room_id=request.POST.get('id_con'))
            context['id_con'] = request.POST.get('id_con')
            return render(request, 'comment_snipset.html', context)
        if request.POST.get('reason') and request.is_ajax():
            print(request.POST)
            new_report = Report.objects.update_or_create(
                report_user=user,
                room=Room.objects.get(id=request.POST.get('id_con')),
                reason=request.POST.get('reason')
            )
            context['comments'] = Comment.objects.filter(room_id=request.POST.get('id_con'))
            context['id_con'] = request.POST.get('id_con')
            return render(request, 'comment_snipset.html', context)

    return render(request, 'comment_snipset.html', context)


class SiteCaredRoom(TemplateView):
    template_name = 'caredRoom.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['caredRoomList'] = CaredRoom.objects.filter(user_id=self.request.user)
        return context


def get_room_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        rooms = Room.objects.filter(
            Q(title__contains=q) |
            Q(address__contains=q)

        ).distinct()
        for room in rooms:
            queryset.append(room)
    return list(set(queryset))
