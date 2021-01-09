"""web_nha_tro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URConf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from signin import views as sign_in_views
from rooms import views as room_views
from room_post import views as post_views
from django.contrib.auth import views as auth_views
from home import views as home_view

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.homeView, name='home'),
    path('caredview/',views.caredView),
    # path('chat', include('chat.urls')),
    path('room/', room_views.SiteRoomView.as_view(), name='room'),
    path(r'room/<int:id>/', room_views.roomDetail, name='roomDetail'),
    path(r'room/postcmt/', room_views.roomDetails),
    path(r'profile/',room_views.postedRoom, name='posted'),
    path(r'phongtro/',room_views.phongtro),
    path(r'ccmn/',room_views.ccmn),
    path(r'nnc/',room_views.nnc),
    path(r'ccnc/',room_views.ccnc),
    path(r'hcm/',room_views.hcm),
    path(r'hn/',room_views.hn),
    path(r'hue/',room_views.hue),
    path(r'danang/',room_views.danang),
    path(r'cantho/',room_views.cantho),

    path('cared/',room_views.SiteCaredRoom.as_view(),name='cared rooms'),

    path(r'login/', sign_in_views.SiteLoginView.as_view(redirect_authenticated_user=True), name='login'),

    path('logout/', sign_in_views.logout, name='logout'),

    path(r'register/', sign_in_views.SiteRegisterView.as_view(), name='register'),
    path('post/', post_views.post, name='post'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
