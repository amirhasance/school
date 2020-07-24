from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars , Tamrin
from django.contrib.auth.models import User

from django.utils.safestring import mark_safe
import json
# Create your views here.
@login_required
def my(request , template_name = 'my_profile/my.html') :
    # import pdb ; pdb.set_trace()

    student = Student.objects.get(user = request.user)


    doroos = Dars.objects.filter(students = student)
    context = {
        "doroos" : doroos,
        "student" : student
    }

    return render(request , template_name , context)

from django.http import JsonResponse
from klass.models import Tamrin , Dars
from klass.serializers import Dars_serializer , Tamrin_serializer

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

def exercise(request , template_name='my_profile/exercise.html' , pk=None):
    pk = pk

    student = Student.objects.get(user = request.user)
    tamrins = Tamrin.objects.all()
    dars = Dars.objects.get(id = pk)
    print(f'excersis = {tamrins}')

    doroos = Dars.objects.filter(students = student)
    context = {
        "doroos" : doroos,
        'dars' : dars,
        'tamrins' : tamrins ,
        "student" : student,
        'pk' : pk,
    }
    
    return render(request , template_name , context)



@login_required
def my_files(request , template_name='my_profile/my_files.html' , pk = None):
    pk = pk

    student = Student.objects.get(user = request.user)


    doroos = Dars.objects.filter(students = student)
    context = {
        "doroos" : doroos,
        "student" : student,
        'pk' : pk,
    }
    

    return render(request, template_name , context)
