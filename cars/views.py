from django.http.response import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from datetime import datetime, timedelta
import json
import threading
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import cars.func as func
from .forms import CommentForm
from .models import Car, Image


# Create your views here.
@login_required
def home_page(request):
    print('redirected from home page')
    return render(request, 'login.html')

@login_required
def index_page(request):
    cars = get_list_or_404(Car)
    return render(request, 'index.html', {'cars':cars})


def logout_page(request):
    try:
        logout(request)
        print('logout_page')
    except KeyError:
        pass
    return render(request, 'login.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user=user)
            print('user logged in')
            return redirect('/index/')
        else:
            print("user not logged in")
            return redirect('login')

    return render(request, "login.html")

@login_required
def car_page(request, model):
    car = get_object_or_404(Car, car_model=model)
    images = get_list_or_404(Image, car_id=car.id)
    print(images)
    if car:
        return render(request, 'car.html', {'car':car, 'images':images, 'range':range(1,len(images))})

@login_required
def compare_page(request):
    result = False
    nocar = False
    args1 = {}
    
    car_name1 = request.GET.get('car1')
    car_name2 = request.GET.get('car2')
    
    if(car_name1 != "" and car_name2 != ""):
      
        try:
            car1 = func.get_car(car_name1)
        except:
            args1 = {"carname": car_name1, "nocar": True}
            return render(request, "choose_compare_page.html", args1)

        try:   
            car2 = func.get_car(car_name2)
        except:
            args1 = {"carname": car_name2, "nocar": True}    
            return render(request, "choose_compare_page.html", args1)
 
        result = func.compare(car1, car2)
        
        return render(request, "compare.html", {'car1': car1, 'car2': car2, 'result': result})
    else:
        print("car has empty field name")
        args2 ={}
        args2["result"] = True
        return render(request, "choose_compare_page.html", args2)


@login_required
def choose_compare_page(request):
    cars = get_list_or_404(Car)
    models = []
    for car in cars:
        models.append(car.car_model)
    return render(request, 'choose_compare_page.html', {'models':models})

@login_required
def car_comment(request, model):
    car = get_object_or_404(Car, car_model=model)
    comments = car.comments.filter(active=True)
    ratings = 0
    average_rating = 0
    if comments:    
        for comment in comments:
            ratings += comment.rating
        average_rating = ratings / len(comments)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, "car_comments.html", {'car': car, 
                                                'comments': comments,
                                                'average_rating': average_rating,
                                                'new_comment':new_comment, 
                                                'comment_form':comment_form})