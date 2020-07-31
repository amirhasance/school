from django.shortcuts import render ,get_object_or_404  , redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars , Tamrin , File_teacher
from django.contrib.auth.models import User
from .forms import Tamrin_Form
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
from klass.models import Tamrin , Dars
from django.views.decorators.csrf import csrf_protect , csrf_exempt
from klass.serializers import Dars_serializer , Tamrin_serializer
# Create your views here.
@login_required
def my(request , template_name = 'my_profile/my.html') :
    # import pdb ; pdb.set_trace()

    student = Student.objects.get(user = request.user)
    tamrins = Tamrin.objects.all()


    doroos = Dars.objects.filter(students = student)
    context = {
        'tamrins':tamrins,
        "doroos" : doroos,
        "student" : student
    }

    return render(request , template_name , context)

@login_required
def teacher(request,template_name = 'my_profile/teacher.html'):
    teacher  = Teacher.objects.get(user = request.user)

    doroos = Dars.objects.filter(teacher = teacher)

    context = {
        'doroos' : doroos,
        'teacher' : teacher
    }

    return render(request , template_name , context)


def ajax(request):
    index = request.GET.get('index')
    this_dars = Dars.objects.get(id = index)
    tamrins = Tamrin_serializer( Tamrin.objects.filter(dars = this_dars) , many =True )
    return JsonResponse({'tamrins': tamrins.data})

from .models import Answer_of_Tamrin_for_every_student
@csrf_exempt
def exercise(request , template_name='my_profile/exercise.html' , pk=None):
    pk = pk
    student = Student.objects.get(user = request.user)
    form = Tamrin_Form(request.POST or None  , request.FILES or None )

    if request.method == "POST":
        print(f'request is post')
        
        if form.is_valid():
            file = form.cleaned_data['file']
            tamrin_id = form.cleaned_data['tamrin']
            tamrin = Tamrin.objects.get(id= tamrin_id)
            ans = Answer_of_Tamrin_for_every_student.objects.create(file = file , tamrin = tamrin , student =student)
            
            

            return redirect(f'/profile/excercise/{pk}')

    # this pk is for this Dars
    
    
    dars = Dars.objects.get(id = pk)
    tamrins = Tamrin.objects.filter(dars = dars)
    for tamrin in tamrins:
        if Answer_of_Tamrin_for_every_student.objects.filter(student = student , tamrin = tamrin).exists():
            tamrin.is_solved = True
        else :
            tamrin.is_solved = False

    doroos = Dars.objects.filter(students = student)

    context = {
        "doroos" : doroos,
        'form': form,
        'dars' : dars,
        'tamrins' : tamrins ,
        "student" : student,
        'pk' : pk,
    }  
    return render(request , template_name , context)


@login_required
def my_files(request , template_name='my_profile/my_files.html' , pk = None):
  
    student = Student.objects.get(user = request.user)
    dars = get_object_or_404(Dars , id = pk)
    doroos = Dars.objects.filter(students = student)
    
    files = File_teacher.objects.filter(dars  = dars)
    
    context = {
        "doroos" : doroos,
        "student" : student,
        'pk' : pk,
        'files' : files,
        'dars' : dars,
    }
    

    return render(request, template_name , context)




def form_html(request , template_name= 'my_profile/form.html'):
    form = Tamrin_Form(request.POST or None , request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            return HttpResponse('form is valid')
        else:
            return HttpResponse('form is not valid')
    
    data = {}
    data['form'] = form
    return render(request , template_name , data)


from exam.models import Exam

def exams(request , template_name= 'my_profile/exams.html' , pk = None):
    student = Student.objects.get(user = request.user)
    dars = get_object_or_404(Dars , id = pk)
    doroos = Dars.objects.filter(students = student)
    
    exams = Exam.objects.filter(dars = dars )
    
    context = {
        "doroos" : doroos,
        "student" : student,
        'pk' : pk,
        'exams' : exams,
        'dars' : dars,
    }
    

    return render(request, template_name , context)

    

