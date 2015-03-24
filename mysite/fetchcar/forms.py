# coding=utf-8
from django import forms
from .models import Brand

brandlist = [brand.name for brand in Brand.objects.all()]

class SelectForm(forms.Form):
	BRANDLIST = zip(brandlist, brandlist)

	brand = forms.ChoiceField(choices=BRANDLIST)