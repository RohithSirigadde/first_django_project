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
    tag       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    report    = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your description",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 20,
                                    'cols': 120
                                }
                            )
                        )
    fare       = forms.DecimalField(initial=199.99)