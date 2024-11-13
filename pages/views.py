from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, World!")

def about(request):  # new
    return render(request, "about.html")