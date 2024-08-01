from django.shortcuts import render , get_object_or_404
from django.shortcuts import HttpResponse
from .models import Customer
from django.template import loader

def login(request):
    
    return render(request , "home/signup.html" , context = {'login' : login} )

def register (request):
    if request.method == "POST":
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        

        
        form = Customer(request.POST.get)
        form.save()
        
        
        return HttpResponse('DATA SAVED')
    else:
        form = Customer()
    return render (request , "home/register.html" , context= {'register' : register})
    

    
    


