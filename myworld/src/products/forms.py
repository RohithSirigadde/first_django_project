from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    tag       = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email	  = forms.EmailField()
    report = forms.CharField(
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
    
    class Meta:
        model = Product
        fields = [
            'tag',
            'report',
            'fare'
        ]


    def clean_tag(self, *args, **kwargs):
    	tag = self.cleaned_data.get('tag')
    	if not "ABCD" in tag:
    		raise forms.ValidationError("This is not a valid title")
    	if not "ae" in tag:
    		raise forms.ValidationError("This is not a valid title")
    	return tag

    def clean_email(self, *args, **kwargs):
    	tag = self.cleaned_data.get("email")
    	if not email.endswith("com"):
    		raise forms.ValidationError("This is not a valid email")
    	return tag


class RawProductForm(forms.Form):
    tag       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    report = forms.CharField(
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