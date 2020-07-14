from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .forms import TestForm , ExamForm , QuestionForm , AnswerForm




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
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Question
def attend(request , template_name = 'exam/attend.html' , exam_pk = None  , question_pk = None):

    this_exam = get_object_or_404(Exam , id = exam_pk)

    ans = AnswerForm(request.POST or None )


    questions = Question.objects.filter(exam = this_exam)

    this = Question.objects.get(id = question_pk)
    # check if this exam of this user has this question ,, question must exist in his exam
    print(this)


    return render(request , template_name , {'exam' : this_exam , 'questions' : questions , 'this' : this , 'ans' : ans})


























def create_exam(request, template_name = 'exam/create_exam.html' ):
    
    
    return render(request , template_name)


def edit_exam(request ,template_name = 'exam/edit_exam.html' , pk = None ):
     
     data = {}
     data['pk'] = pk
     return render(request , template_name ,  data)