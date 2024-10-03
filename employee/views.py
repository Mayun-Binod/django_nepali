from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("this is home/index page")

def employee(request):
    return HttpResponse("this is employee page")