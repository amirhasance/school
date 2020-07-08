from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from klass.models import Student , Teacher , Dars
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

def ajax(request):
    index = request.GET.get('index')
    this_dars = Dars.objects.get(id = index)
    tamrins = Tamrin_serializer( Tamrin.objects.get(dars = this_dars)  )
    return JsonResponse({'tamrins': tamrins.data})




