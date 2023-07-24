from django import forms

from .models import Product

class ProductFormDetails(forms.ModelForm):
	class Beta:
		model = Product
		fields= [
			'tag',
			'report',
			'fare'
		]