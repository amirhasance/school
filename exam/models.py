from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from klass.models import Student , Teacher , Dars
from school_home.views import file_size
from django.core.validators import MinValueValidator, MaxValueValidator


class Exam(models.Model):
    
    name = models.CharField(max_length = 500)
    time_starts = models.DateTimeField()
    time_ends = models.DateTimeField()
    dars = models.ForeignKey(Dars , on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Exam = {self.name} , {self.dars} '
    
    class Meta:
        verbose_name_plural = 'امتحانات'
    
    
    


class Question(models.Model):
    
    name = models.CharField(max_length = 300 , null =True , blank=True)
    number = models.IntegerField(default=1 , null=False)
    question = models.CharField(max_length=500  , blank= False , null = False)
    image = models.ImageField(upload_to = 'questions/test' , null =True , blank = True)
    # caution_help = models.CharField(max_length=500  , blank= False , null = False)
    exam = models.ForeignKey(Exam , on_delete=models.CASCADE)
    time_considered_to_solve_in_seconds = models.IntegerField(default=1)
    
   
    choice_one = models.CharField(max_length=500 , null=True , blank = True)
    choice_two = models.CharField(max_length=500 , null= True , blank = True)
    choice_three = models.CharField(max_length=500 , null = True , blank = True)
    choice_four = models.CharField(max_length=500 , null = True , blank = True)
    correct_ans = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(4)] )
    
    class Meta:
        ordering = ('number' , )
        verbose_name_plural = 'سوالات'
    
    
    def __str__(self):
        return self.question 



class WQuestion(models.Model):
    name = models.CharField(max_length = 300 , null =True , blank=True)
    number = models.IntegerField(default=1 , null=False)
    question = models.CharField(max_length=500  , blank= False , null = False)
    image = models.ImageField(upload_to = 'questions/tashrihi' , null =True , blank = True)
    # caution_help = models.CharField(max_length=500  , blank= False , null = False)
    exam = models.ForeignKey(Exam , on_delete=models.CASCADE)
    Time_considered_to_solve_in_seconds = models.IntegerField(default=1)

    class Meta:
        ordering = ('number' , )
        verbose_name_plural = 'سوالات تشریحی'

    def __str__(self):
        return self.question
    
    




    

    
    
class Answer(models.Model):
    
    answer = models.CharField(max_length=500  , null=True , blank = True)
    
    question = models.ForeignKey(Question , on_delete=models.CASCADE , null =False , )
    
    image = models.ImageField(upload_to='answers' , validators=[file_size , ])
    
    selected_choice = models.CharField( max_length = 500 , null=True , blank=True)
    
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    
    is_seened = models.BooleanField(default=False)
    
    is_solved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('question__number',)
        verbose_name_plural = 'پاسخ ها'
    
    def __str__(self):
        return f'answer , {self.answer} , {self.question}'
    
    
    

class TestModel(models.Model):
    name = models.CharField(max_length = 200)
    date_time = models.DateTimeField()
    date = models.DateField()

    def __str__(self):
        return self.name

    
 
