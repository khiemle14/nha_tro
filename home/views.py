from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from rooms.models import Room, CaredRoom
from rooms.views import get_room_queryset


def homeView(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
        print(query)
        context['searched'] = get_room_queryset(query)
        print(get_room_queryset(query))
        return render(request, 'serach_snipset.html', context)
    print(query)
    context['roomList1'] = Room.objects.order_by('-viewed')[:4]
    context['roomList2'] = Room.objects.filter(type_id=1).order_by('id')[:5]
    context['roomList3'] = Room.objects.filter(type_id=2).order_by('id')[:5]
    context['roomList4'] = Room.objects.filter(type_id=3).order_by('id')[:5]
    context['roomList5'] = Room.objects.filter(type_id=4).order_by('id')[:5]
    context['hanoi_roomlist'] = get_room_queryset('Hà nội')

    return render(request, 'index.html', context)


def caredView(request):
    context = {}
    roomlist=[]
    if request.GET and request.is_ajax():
        print(request.GET)
        caredlist = CaredRoom.objects.filter(user_id=request.user).distinct()
        for room in caredlist:
            roomlist.append(room)

        context['cared_roomlist']=list(set(roomlist))
        print(context['cared_roomlist'])
        return render(request,'cared.html',context)
