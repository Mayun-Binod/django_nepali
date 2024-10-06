from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeerForm
# Create your views here.

def employeer(request):
    form=EmployeerForm()
    context={
        'form':form
    }
    if request.method=='POST':
        form=EmployeerForm(request.POST)
        print(form.is_valid())
        data=form.cleaned_data
        print(data['name'])  
    return render(request,'employeer/employeer.html',context)



# def employeer(request):
     
    # return HttpResponse("this is employee page")
    # context = {
    #  'person1': {
    #     'name': 'Alice',
    #     'age': 25,
    #     'city': 'New York'
    #  },
    #  'person2': {
    #     'name': 'Bob',
    #     'age': 30,
    #     'city': 'Los Angeles'
    #  },
    #  'person3': {
    #     'name': 'Charlie',
    #     'age': 35,
    #     'city': 'Chicago'
    #  }
    #  }
    # get
    # data=request.GET
    # print(data)
    # email=data['email']
    # print(email)
    # # post
    #  data=request.POST
    # print(data)
    # email=data['email']
    # print(email)
    # return render(request,'employeer/employeer.html')