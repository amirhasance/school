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




from .models import Exam
from klass.models import Student
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question
from django.views.decorators.csrf import csrf_protect , csrf_exempt


@csrf_exempt
def attend(request , template_name = 'exam/attend.html' , exam_pk = None  , question_pk = None):

    this_exam = get_object_or_404(Exam , id = exam_pk)

    if  not this_exam.can_attend:
        return HttpResponse('time out ')

    questions = Question.objects.filter(exam = this_exam) 

    questions_count = questions.count()

    this = Question.objects.get(id = question_pk)

    user = request.user

    student = get_object_or_404(Student , user = user)

    print(this)

    time = timezone.now()

    if request.method == 'POST':
        
        file = request.FILES['file']
        user = request.user


    

    data = {

        'exam' : this_exam ,
        'questions' : questions , 
        'this' : this  ,
        'time': time,
        'num' : questions_count,
        'student' : student
        
            }





    return render(request , template_name , data)


























def create_exam(request, template_name = 'exam/create_exam.html' ):
    
    
    return render(request , template_name)


def edit_exam(request ,template_name = 'exam/edit_exam.html' , pk = None ):
     
     data = {}
     data['pk'] = pk
     return render(request , template_name ,  data)