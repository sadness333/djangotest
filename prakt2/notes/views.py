from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Notes
from django.contrib.auth import authenticate, login, logout
import time
# Create your views here.

def add_notes(request):
    if request.method == "POST":
        user=request.user
        data=request.POST
        content = data.get('note-text')
        Notes.objects.create(user=user, content=content)
    return render(request,"add_notes.html")

def notes(request):
    user=request.user
    user_notes= Notes.objects.filter(user=user)
    return render(request,'notes.html',{'user_notes':user_notes})

def logout_page(request):
    if request.method == "GET":
        logout(request)
        return HttpResponseRedirect("reg/")

def login_page(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return HttpResponse("<h3>Пользователь с таким логином и паролем не найден</h3>")
            login(request, user)
            return HttpResponse("<h3>Вы успешно авторизованы</h3>")
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")



def reg(request):
    if request.method == "GET":
        return render(request, "reg.html")
    else:
        data = request.POST
        new_username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password1, password2 = data.get("password1"), data.get("password2")
        if new_username is None:
            return HttpResponse("<h3>Введите имя пользователя</h3>")
        elif email is None:
            return HttpResponse("<h3>Введите почту</h3>")
        elif User.objects.filter(username=new_username).exists():
            return HttpResponse("Имя пользователя уже занято.", status=400)  # 400 Bad Request
        elif first_name is None:
            return HttpResponse("<h3>Введите ваше имя</h3>")
        elif last_name is None:
            return HttpResponse("<h3>Введите вашу фамилию</h3>")
        elif password1 is None or password2 is None:
            return HttpResponse("<h3>Введите пароль</h3>")
        elif password1 != password2:
            return HttpResponse("<h3>Пароли должны совпадать</h3>")
        else:
            newuser = User()
            newuser.create_user(new_username,first_name,last_name, email, password1)
            return HttpResponse("<h3>Вы успешно зарегистрировались</h3>")
    