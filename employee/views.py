from django.shortcuts import render
from django.http import HttpResponse
from employee.forms import EmployeeForm
# Create your views here.

def index(request):
    # return HttpResponse('this is index page')
    return render(request,'base.html')


def employee(request):
    if request.method=='POST':
        pass
        # data=request.POST
        # first_name=data['first_name']
        # print(first_name)
        # last_name=data['last_name']
        # print(last_name)
        # address=data['address']
        # print(address)
        # context={
        #     'first_name':first_name,
        #     'last_name':last_name,
        #     'address':address,
        # }
    else:
        form=EmployeeForm()
        context={
            'form':form
        }
    # return HttpResponse("this is employee page")
    # if request.method == 'POST':  # Correcting 'POSt' to 'POST'
    #     data = request.POST
    #     email = data['email']
    #     password = data['password']
    #     context = {
    #         'name': email,
    #         'address': password,
    #     }
    # else:
    #     context = {
    #         'name': "Binod",
    #         'address': "Lalitpur",
    #     }

    return render(request, 'employee/employee.html', context)