from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("this is first project!!")

def greet(request):
    return HttpResponse("Helllo good morning")