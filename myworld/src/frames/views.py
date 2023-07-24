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
 	# return render(request, "contact.html", {})

def detail_view(request, *args, **kwargs):
    my_context = {
        "my_description": "abc this is about us",
        "my_num": 123,
        "my_list": [1313, 4231, 312, "Abc"]
    }
    return render(request, "detail.html", my_context)

