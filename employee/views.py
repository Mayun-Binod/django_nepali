from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('this is index page')
    return render(request,'base.html')


def employee(request):
    # return HttpResponse("this is employee page")
     return render(request,'employee/employee.html')