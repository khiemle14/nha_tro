from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

# Create your views here.
from django.db import connection
from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView

from user.models import OwnerUser


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))
    # remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'required':False}))


class SiteLoginView(LoginView):
    template_name = 'dangnhap.html'
    authentication_form = CustomLoginForm

    # def form_valid(self, form):
    #     remember_me = form.cleaned_data['remember_me']
    #     login(self.request, form.get_user())
    #
    # return super(LoginView, self).form_valid(form)


class RegisterForm(UserCreationForm):
    class Meta:
        model = OwnerUser
        fields = ("full_name", "username", "email", "phone_number", "is_owner")
        field_classes = {'username': UsernameField}
        widgets = {
        }

    # def test_sql_connection():
    #     with connection.cursor() as cursor:
    #         cursor.execute("select * from user_owneruser, [self.baz]")
    #         row = cursor.fetchone()
    #
    #     return row


class SiteRegisterView(FormView):
    template_name = 'dangky.html'
    form_class = RegisterForm

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return super(SiteRegisterView, self).get(request)

    def post(self, request, **kwargs):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                messages.info(self.request, "Thanks for registering. You are now logged in.")
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(self.request, new_user)
                return redirect(reverse('home'), {"alert": "Cảm ơn bạn đã tin tưởng và sử dụng dịch vụ của chúng tôi"})
        else:
            return redirect(reverse('register'))
        return redirect(reverse('register'))
    # def form_valid(self, form):
    #     data = form.cleaned_data
    #     new_user = OwnerUser.objects.create_user(full_name=data['full_name'],
    #                                              username=data['username'],
    #                                              phone_number=data['phone_number'],
    #                                              email=data['email'],
    #
    #                                              password=data['password1'],
    #                                              is_owner=data['is_owner']
    #                                              )
    #     return redirect(reverse('home'))


def logout(request):
    auth.logout(request)
    return redirect('/')
