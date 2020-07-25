from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars , Tamrin
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from klass.models import Tamrin , Dars
from django.views.decorators.csrf import csrf_protect , csrf_exempt
# Create your views here.

@login_required
def teacher_home(request , template_name = 'teacher_profile/my.html'):

    user = request.user
    if  not Teacher.objects.filter(user = user).exists():
        return HttpResponse('you are not allowed')


    return render(request , template_name )


