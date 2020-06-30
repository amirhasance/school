from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars
from django.contrib.auth.models import User
from .serializers import Doroos_serializer , Student_serializer
from django.utils.safestring import mark_safe
import json
# Create your views here.
@login_required
def my(request , template_name = 'my_profile/my.html') :

    student = Student.objects.get(user = request.user)


    doroos = Dars.objects.filter(students = student) 
    context = {
        "doroos" : doroos,
        "student" : student
    }

    return render(request , template_name , context)





