from django.shortcuts import render ,redirect
from .forms import login_Form
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , login , logout
# Create your views here.

@csrf_exempt
def site_login(request ,template_name='login/login.html' ):
   
   form = login_Form(request.POST or None)
   if request.user.is_authenticated :
       return redirect('/profile/my')
    #    return redirect('/../profile/')
      

   
   if request.method == 'POST':
       if form.is_valid() : 
        #    print(form.cleaned_data.get('username'))
        #    print(form.cleaned_data.get('password'))
           
           user = authenticate(request=request , username =form.cleaned_data.get('username'),password = form.cleaned_data.get('password')  )
           login(request , user)
           return redirect('../profile/my')
       else :
            return HttpResponse('form is not valid')
   else :
        return render(request , template_name , {'form' : form})


def log_out(request):
    logout(request)
    return redirect('/')
      
def site_logout(request , template_name = 'login/logout.html'):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/../')
    
   
        
        

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
    

