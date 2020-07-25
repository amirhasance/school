from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars , Tamrin
from django.contrib.auth.models import User
from .forms import Tamrin_Form
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
from klass.models import Tamrin , Dars
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

def exercise(request , template_name='my_profile/exercise.html' , pk=None):
    pk = pk
    # form = Tamrin_Form(request.POST or None  )

    # if request.method == "POST":
    #     print(f'request is post')
    #     import pdb ; pdb.set_trace()
    #     if form.is_valid():
    #         import pdb ; pdb.set_trace()
    #         return HttpResponse('form is valid')

    # this pk is for this Dars
    student = Student.objects.get(user = request.user)
    
    dars = Dars.objects.get(id = pk)
    tamrins = Tamrin.objects.filter(dars = dars)

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
    pk = pk

    student = Student.objects.get(user = request.user)


    doroos = Dars.objects.filter(students = student)
    context = {
        "doroos" : doroos,
        "student" : student,
        'pk' : pk,
    }
    

    return render(request, template_name , context)




def form_html(request , template_name= 'my_profile/form.html'):
    form = Tamrin_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            return HttpResponse('form is valid')
        else:
            return HttpResponse('form is not valid')
    
    data = {}
    data['form'] = form
    return render(request , template_name , data)