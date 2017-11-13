from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')
    # return HttpResponse("success")


def app(request):
    return render(request, 'app.html')