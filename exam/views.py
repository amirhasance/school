from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from .forms import TestForm , ExamForm

def index(request , template_name = 'exam/index.html'):

    form = ExamForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            from django.http import HttpResponse
            return HttpResponse('Time is  created')
        else :
            return HttpResponse('form is not valid')
    

    return render(request , template_name , { 'name' : 'amir' , 'form':form})



def create_exam(request, template_name = 'exam/create_exam.html' ):
    
    
    return render(request , template_name)


def edit_exam(request ,template_name = 'exam/edit_exam.html' , pk = None ):
     
     data = {}
     data['pk'] = pk
     return render(request , template_name ,  data)