from django.shortcuts import render

# Create your views here.
from .models import Product

def product_details_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 'tag':obj.tag,
	# 'report':obj.report
	# }
	context = {
		'object': obj
	}
	return render(request, "product/details.html", context)