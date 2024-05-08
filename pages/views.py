from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.utils.timezone import now
import random
import string
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

def home_page(request):
    return render(request,'index.html')

def tapchans(request):
    tapchan = Tapchan.objects.all()

    return render(request,'tapchans.html', {"tapchan":tapchan})

def tapchan(request, id):
    tapchan = Tapchan.objects.get(id=id)
    menu = Menu.objects.all()
    if request.method == "POST":
        tapchan = Tapchan.objects.get(id=id)
        tapchan_i = tapchan.name
        person = request.POST.get("name")
     
        number  = request.POST.get("number_phone")
     
        food = ""
        if any('summ' in key for key in request.POST):
            for key, value in request.POST.items():
                if 'summ' in key:
                    
                    name = key.split('_')[1]  
                    colvo = value
                    food = food + str(name) + " - " +str(colvo) + "; "
        name_order = "Номер заказа: " + ''.join(random.choices(string.ascii_letters, k=2)) + str(''.join(random.choices('0123456789', k=4)))
        date_rec = request.POST.get("date_rec")
        
        order = Order.objects.create(name=name_order, tapchan=tapchan_i,person=person, number=number, food=food, date_rec=date_rec )
       
        try:
          send_mail(
                    name_order,
                    "У вас новый заказ: " + name_order  + "\n" +
                    "Имя:  " + person + "\n" +
                    "Номер телефона: " +number + "\n" +
                    "Тапчан: "+ tapchan_i + "\n" +
                    "Предзаказ еды: "+ food + "\n" +
                    "На дату и время: "+ date_rec + "\n",
                    EMAIL_HOST_USER,
                    ["ilyostream@gmail.com"]
                )
        except:
            pass
        
        return redirect('order', order.id)
    return render(request,'menu.html', {"tapchan":tapchan, "menu":menu})



def order(request, id):
    order = Order.objects.get(id=id)
    return render(request,'check.html', {"order":order})