from django.shortcuts import render
from .models import details
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def login(request):
    return render(request,'first.html')
def home(request):
    return render(request,'success.html')
def add(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('password') and request.POST.get('phnnumber'):
                enter=details()
                enter.email= request.POST.get('email')
                enter.password= request.POST.get('password')
                enter.phone= request.POST.get('phnnumber')

                enter.save()
                
                return HttpResponseRedirect('success/')  
                
    else:
            return render(request,'register.html')

def fetch(request):
    
    if request.method=="POST":
        if request.POST.get('s_email') and request.POST.get('s_password'):
            data = details.objects.all()
            for i in data:
                if i.email==request.POST.get('s_email') and i.password==request.POST.get('s_password'):
                    return HttpResponseRedirect('first/')  
        else:
            return HttpResponse("username or password you entered is incorrect")
    else:
        return render(request,'home.html')
                    
        





                  

    
# Create your views here.
