from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields= [
			'tag',
			'report',
			'fare'
		]


class RawProductForm(forms.Form):
    tag       = forms.CharField()
    report    = forms.CharField()
    fare       = forms.DecimalField(initial=199.99)