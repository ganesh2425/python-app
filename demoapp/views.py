from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("this is first demoapp")

def about(request):
    return HttpResponse("thanks watching my reels")