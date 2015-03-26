from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fetchcar.models import Car, Brand
from fetchcar.forms import SelectForm

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


'''def search(request):
		context = {'state': None, "brands": Brand.objects.all().order_by('name')}
		if 'brand' in request.POST:
			print(request.POST['country'])

		return render_to_response("fetchcar/search.html", context)'''

def search(request):
	form = SelectForm
	return render_to_response("fetchcar/search.html", dict(form=form))