# coding=utf-8
from django import forms
#from .models import Brand, CarType



#brandlist = [(brand.id, brand.name) for brand in Brand.objects.all()]

class SelectForm(forms.Form):
	#BRANDLIST = [(None, u'请选择品牌')] + brandlist
	#brand = forms.ChoiceField(choices=BRANDLIST)
	cartype = forms.CharField()