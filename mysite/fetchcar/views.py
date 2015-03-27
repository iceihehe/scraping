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
	regtime_list = list(set([car.reg_time for car in Car.objects.all()]))
	regtime_list.sort(reverse=True)
	if request.method == "POST":
		form = Form(request.POST)
		cartype_id = form.data.get("cartype")
		if not cartype_id:
			car_list = Car.objects.all()
		else:
			cartype = CarType.objects.filter(id=cartype_id).first()
			car_list = Car.objects.filter(car_type=cartype).all()
		regtime = form.data.get("regtime")
		if regtime:
			car_list = car_list.filter(reg_time=regtime).all()
		price_min = form.data.get("price_min")
		if price_min:
			car_list = car_list.filter(price__gt=int(price_min)*10000).all()
		price_max = form.data.get("price_max")
		if price_max:
			car_list = car_list.filter(price__lt=int(price_max)*10000).all()

		return render_to_response("fetchcar/search.html", dict(car_list=car_list, regtime_list=regtime_list), RequestContext(request))
	return render_to_response("fetchcar/search.html",  dict(regtime_list=regtime_list), RequestContext(request))


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
