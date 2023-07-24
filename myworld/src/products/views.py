from django.shortcuts import render

from .forms import ProductForm
# Create your views here.
from .models import Product

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm

	obj = Product.objects.get(id=1)
	# context = {
	# 'tag':obj.tag,
	# 'report':obj.report
	# }
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)

def product_details_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 'tag':obj.tag,
	# 'report':obj.report
	# }
	context = {
		'object': obj
	}
	return render(request, "products/product_detail.html", context)