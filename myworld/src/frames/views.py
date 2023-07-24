from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def mainScreen_view(*args, **kwargs):
	return HttpResponse("<h1>This is main screen/ home screen</h1>")