from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from klass.models import Student , Teacher , Dars

#TODO  : Try pip install django_cleanup , https://stackoverflow.com/questions/16041232/django-delete-filefield
class Exam(models.Model):
    
    name = models.CharField(max_length = 500)
    Time_starts = models.DateTimeField(auto_now_add=True)
    Time_expires = models.DateTimeField(auto_now_add=False)
    dars = models.ForeignKey(Dars , on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Exam = {self.name} , {self.dars} '
    
    


class Question(models.Model):
    
    name = models.CharField(max_length = 300 , null =True , blank=True)
    number = models.IntegerField(default=1 , null=False)
    question = models.CharField(max_length=500  , blank= False , null = False)
    image = models.ImageField(upload_to = 'questions' , null =True , blank = True)
    caution_help = models.CharField(max_length=500  , blank= False , null = False)
    Barem = models.IntegerField()
    exam = models.ForeignKey(Exam , on_delete=models.CASCADE)
    Time_considered_to_solve_in_minute = models.IntegerField(default=1)
    
   
    choiceOne = models.CharField(max_length=500 , null=True , blank = True)
    choiceTwo = models.CharField(max_length=500 , null= True , blank = True)
    choiceThree = models.CharField(max_length=500 , null = True , blank = True)
    choiceFour = models.CharField(max_length=500 , null = True , blank = True)
    
    class Meta:
        ordering = ('number' , )
    
    
    def __str__(self):
        return self.question 
    
    
class Answer(models.Model):
    
    answer = models.CharField(max_length=500  , null=True , blank = True)
    
    question = models.ForeignKey(Question , on_delete=models.CASCADE , null =False , )
    
    image = models.ImageField(upload_to='answers')
    
    selected_Choice = models.CharField( max_length = 500 , null=True , blank=True)
    
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    
    Is_seened = models.BooleanField(default=False)
    
    Is_Solved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('question__number',)
    
    def __str__(self):
        return f'answer , {self.answer} , {self.question}'
    
    
    

    
 

    