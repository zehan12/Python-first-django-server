from django.http import HttpResponse
from django.shortcuts import render


def index( request ):
    return HttpResponse("Hello from Backend");

def about( request ):
    # return HttpResponse("welcome to about")
    return render(request,'files/about.html',{'data':"test-data"})