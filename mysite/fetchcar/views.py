from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from fetchcar.models import Car
from fetchcar.forms import SelectForm
# Create your views here.


def index(request):
	if request.method == "POST":
		form = SelectForm(request.POST)
		return render_to_response("fetchcar/index.html")
	form = SelectForm()
	return render_to_response("fetchcar/index.html", dict(form=form),
                              RequestContext(request))


def detail(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if car is None:
        return render_to_response("fetchcar/404.html")
    return render_to_response("fetchcar/detail.html", dict(car=car))
