from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars
# Create your views here.
@login_required
def my(request , template_name = 'my.html') :
    # import pdb ; pdb.set_trace()
    return HttpResponse(f'{request.user.username}')


