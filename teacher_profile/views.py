from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars , Tamrin
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from klass.models import Tamrin , Dars
from django.views.decorators.csrf import csrf_protect , csrf_exempt
from .forms import Create_Tamrin_Form
# Create your views here.

@login_required
def teacher_home(request , template_name = 'teacher_profile/my.html'):


    user = request.user
    teacher = user.teacher
    if  not Teacher.objects.filter(user = user).exists():
        return HttpResponse('you are not allowed')


    doroos = Dars.objects.filter(teacher = teacher)




    data = {
        'doroos' : doroos
    }


    return render(request , template_name , data )

    

@login_required
def excercise(request, template_name='teacher_profile/excercise.html' , pk = None):

    teacher = Teacher.objects.get(user =request.user)
    dars = Dars.objects.get(id = pk)
    tamrins = Tamrin.objects.filter(dars = dars)


    doroos = Dars.objects.filter(teacher = teacher)
    form = Create_Tamrin_Form()


    data = {
         'tamrins':tamrins,
         'doroos' : doroos,
          'form' : form,
          'dars' : dars,
        
    }

    return render(request , template_name , data)



@login_required
def files(request, template_name='teacher_profile/files.html' , pk = None):

    



    data = {


    }

    return render(request , template_name , data)












from django.shortcuts import get_object_or_404 , redirect

@login_required
@csrf_exempt
def excercise_create_new(request , template_name='teacher_profile/excercise_create_new.html' , pk = None):

    #this pk is id of DARS 
    dars = get_object_or_404(Dars , id = pk)
    form = Create_Tamrin_Form(request.POST or None , request.FILES or None)

    if request.method == 'POST':
        
        if form.is_valid():
            this_tamrin = Tamrin()
            name = form.cleaned_data['name']
            # time_created = form.cleaned_data['time_created']
            time_expire = form.cleaned_data['time_expire']
            file = form.cleaned_data['file']
            Tamrin.objects.create(name = name , time_expire = time_expire , file = file , dars = dars)
    
            return redirect(f'/teacher/excercise/{pk}')


    

    data = {
        'pk' : pk,
        'dars' : dars,
        'form' : form,


    }



    return render(request , template_name , data)





















@login_required
def excercise_edit(request , template_name='teacher_profile/excercise_edit.html' , pk = None):

    data = {
        'pk' : pk,



    }



    return render(request , template_name , data)
