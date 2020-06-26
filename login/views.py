from django.shortcuts import render
from .forms import login_Form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , login
# Create your views here.
@csrf_exempt
def login(request ,template_name='login/login.html' ):
   form = login_Form(request.POST or None)
   if request.method == 'POST':
       if form.is_valid() : 
           print(form.cleaned_data.get('username'))
           print(form.cleaned_data.get('password'))
           return HttpResponse('from is valid')
           #set session and anothers for a student

       else :
            return HttpResponse('form is not valid')
   else :
        return render(request , template_name , {'form' : form})
      
    
    
   
        
        

def tlogin(request , template_name='login/tlogin.html'):
    pass


def alogin(request , template_name='login/alogin.html'):
   form = login_Form(request.POST or None)
   if request.method == 'POST':
       if form.is_valid() : 
           print(form.cleaned_data.get('username'))
           print(form.cleaned_data.get('password'))
           return HttpResponse('from is valid')
           #set session and anothers for a student

       else :
            return HttpResponse('form is not valid')
   else :
        return render(request , template_name , {'form' : form})
      