import json
from django.http import HttpResponse
from django.forms import Form
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fetchcar.models import Car, Brand, CarType

# Create your views here.


def index(request):
	car_list = Car.objects.order_by('-id')
	paginator = Paginator(car_list, 20)
	page = request.GET.get('page')
	try:
		cars = paginator.page(page)
	except PageNotAnInteger:
		cars = paginator.page(1)
	except EmptyPage:
		cars = paginator.page(paginator.num_pages)
	return render_to_response("fetchcar/index.html", dict(car_list=cars))


def detail(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if car is None:
        return render_to_response("fetchcar/404.html")
    return render_to_response("fetchcar/detail.html", dict(car=car))


def search(request):
	if request.method == "POST":
		form = Form(request.POST)
		cartype = CarType.objects.filter(id=form.data.get('cartype')).first()
		print(cartype.name)
		car_list = Car.objects.filter(car_type=cartype).all()
		paginator = Paginator(car_list, 20)
		page = request.GET.get('page')
		try:
			cars = paginator.page(page)
		except PageNotAnInteger:
			cars = paginator.page(1)
		except EmptyPage:
			cars = paginator.page(paginator.num_pages)
		return render_to_response("fetchcar/index.html", dict(car_list=cars))
	return render_to_response("fetchcar/search.html", RequestContext(request))


def cartype_api(request):
	para = request.GET.get('brandid', 0)

	if not para:
		cartype_list = CarType.objects.all()
	else:
		brand = Brand.objects.filter(id=para)
		cartype_list = CarType.objects.filter(brand=brand).all()
	res = []
	for cartype in cartype_list:
		res.append(dict(id=cartype.id, name=cartype.name))

	return HttpResponse(json.dumps(dict(cartypes=res)))

def brand_api(request):
	res = []
	brand_list = Brand.objects.all()
	for brand in brand_list:
		res.append(dict(id=brand.id, name=brand.name))
	return HttpResponse(json.dumps(dict(brands=res)))