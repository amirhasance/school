from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
# Create your views here.

def index(request , template_name = 'exam/index.html'):
    
    data = {}
    return render(request , template_name , data)
def create_exam(request, template_name = 'exam/create_exam.html' ):
    
    
    return render(request , template_name)


def edit_exam(request ,template_name = 'exam/edit_exam.html' , pk = None ):
     
     data = {}
     data['pk'] = pk
     return render(request , template_name ,  data)