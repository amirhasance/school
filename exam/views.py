from django.shortcuts import render , redirect , get_object_or_404
from django.utils.safestring import mark_safe
import json
from .forms import TestForm , ExamForm 
from klass.models import Teacher , Student  , Dars
from .models import Exam
from django.utils import timezone
from .models import Question , WQuestion
from django.views.decorators.csrf import csrf_protect , csrf_exempt
from django.http import JsonResponse

def index(request , template_name = 'exam/index.html' , pk = None):
    form = ExamForm(request.POST or None)
    user = request.user
    teacher = get_object_or_404(Teacher , user = user)
    dars = get_object_or_404(Dars , id = pk , teacher = teacher)

    if request.method == 'POST':
        if form.is_valid():

            name = form.cleaned_data['name']
            time_starts = form.cleaned_data['time_starts']
            time_ends = form.cleaned_data['time_ends']
            exam = Exam.objects.create(name = name , dars = dars , time_starts = time_starts , time_ends = time_ends)
            from django.http import HttpResponse
            return redirect(f'/teacher/exam/create_new/{exam.id}')
        else :
            return HttpResponse('Exam not  Created')
    

    return render(request , template_name , {   'form':form  , })


@csrf_exempt
def attend(request , template_name = 'exam/attend.html' , exam_pk = None  , question_pk = None):

    this_exam = get_object_or_404(Exam , id = exam_pk)

    if  not this_exam.can_attend:
        return HttpResponse('time out ')

    questions = Question.objects.filter(exam = this_exam) 

    wquestions = WQuestion.objects.filter(exam = this_exam)

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
        'wquestions' : wquestions,
        'this' : this  ,
        'time': time,
        'num' : questions_count,
        'student' : student ,

  
            }

    return render(request , template_name , data)


@csrf_exempt
def addq(request , template_name='exam/addq.html' , pk=None):

    user = request.user
    teacher = get_object_or_404(Teacher , user = user)
    exam = get_object_or_404(Exam , id = pk)

    if request.method == "POST":
        file = request.FILES['file']
        post_data = request.POST
        question = post_data['question']
        choice_one = post_data['choice_one']
        choice_two = post_data['choice_two']
        choice_three = post_data['choice_three']
        choice_four =  post_data['choice_four']
        correct_ans = post_data['correct_ans']
       
        Question.objects.create(exam  = exam , image = file , question = question , choice_four = choice_four , choice_one = choice_one , choice_two = choice_two , choice_three = choice_three , correct_ans = correct_ans)
        return JsonResponse({'message' : 'ok' } , status = 200)     
    

    data ={
     
        'exam' : exam,
    }

    return render(request , template_name , data)



@csrf_exempt
def addwq(request , template_name='exam/addwq.html' , pk=None):
    user = request.user
    teacher = get_object_or_404(Teacher , user = user)
    exam = get_object_or_404(Exam , id = pk)

    if request.method == "POST":
        file = request.FILES['file']
        post_data = request.POST
        question = post_data['question']
        WQuestion.objects.create(exam = exam , image = file  , question = question )
        return JsonResponse({'message' : 'ok' } , status = 200)

    data ={
    'exam' : exam ,
    }

    return render(request , template_name , data)









def start_exam(request , exam_pk = None):

    exam = get_object_or_404(Exam , id = exam_pk)

    if Question.objects.filter(exam  = exam ).exists():
         first = Question.objects.filter(exam=exam).first()
    else :
        first = WQuestion.objects.filter(exam =exam).first()

    return redirect(f'/exam/attend/{exam_pk}/{first.id}')
    


























def create_exam(request, template_name = 'exam/create_exam.html' ):
    
    
    return render(request , template_name)


def edit_exam(request ,template_name = 'exam/edit_exam.html' , pk = None ):
     
     data = {}
     data['pk'] = pk
     return render(request , template_name ,  data)