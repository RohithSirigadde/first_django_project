from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainScreen_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1>This is main screen/ home screen</h1>")
	return render(request, "main.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})
	# print(args, kwargs)
	# print(request.user)
 # 	return render(request, "contact.html", {})

def detail_view(request, *args, **kwargs):
	return render(request, "detail.html", {})
