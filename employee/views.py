from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('this is index page')
    return render(request,'base.html')


def employee(request):
    # return HttpResponse("this is employee page")
    if request.method == 'POST':  # Correcting 'POSt' to 'POST'
        data = request.POST
        email = data['email']
        password = data['password']
        context = {
            'name': email,
            'address': password,
        }
    else:
        context = {
            'name': "Binod",
            'address': "Lalitpur",
        }

    return render(request, 'employee/employee.html', context)