from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainScreen_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return HttpResponse("<h1>This is main screen/ home screen</h1>")


def contact_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	return HttpResponse("<h1>This is contact screen</h1>")