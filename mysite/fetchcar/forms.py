# coding=utf-8
from django import forms


class SelectForm(forms.Form):
	OPTIONS = (
		("a","a"),
		("b","b")
		)
	brand = forms.MultipleChoiceField(choices=OPTIONS)