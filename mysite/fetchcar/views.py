from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from fetchcar.models import Car
from fetchcar.forms import SelectForm
from datetime import date
# Create your views here.


def index(request):
	car_list = Car.objects.order_by('-id')
	return render_to_response("fetchcar/index.html",dict(car_list=car_list))


def detail(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if car is None:
        return render_to_response("fetchcar/404.html")
    return render_to_response("fetchcar/detail.html", dict(car=car))
