from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from klass.models import Student , Teacher , Dars
from school_home.views import file_size
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_ans(value):
    status = value>0 and value<5

    if not status:
        raise ValidationError(
             _('%(value)s is not correct'),
             params = {'value' : value}
        )
        



class Exam(models.Model):
    
    name = models.CharField(max_length = 500)
    time_starts = models.DateTimeField()
    time_ends = models.DateTimeField()
    dars = models.ForeignKey(Dars , on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'Exam = {self.name} , {self.dars} '

    def is_expired(self):
        return timezone.now() > self.time_ends
    
    def can_attend(self):
        return (timezone.now() > self.time_starts ) and ( timezone.now() < self.time_ends )

    
    class Meta: 
        verbose_name_plural = 'امتحانات'
        ordering = ('-time_starts' , )
    

   

class Question(models.Model):
    

    question = models.CharField(max_length=500  , blank= False , null = False)
    image = models.ImageField(upload_to = 'questions/test' , null =True , blank = True)
    # caution_help = models.CharField(max_length=500  , blank= False , null = False)
    exam = models.ForeignKey(Exam , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    choice_one = models.CharField(max_length=150 , null=True , blank = True)
    choice_two = models.CharField(max_length=150 , null= True , blank = True)
    choice_three = models.CharField(max_length=150 , null = True , blank = True)
    choice_four = models.CharField(max_length=150 , null = True , blank = True)
    correct_ans = models.IntegerField(validators=[validate_ans , ])

    def __str__(self):
        return self.question 
    
    def summery(self):
        return '...' + self.question[:20] 

    class Meta:
        ordering = ('-date' , )
        verbose_name_plural = ' سوالات تستی'
    


class WQuestion(models.Model):

    question = models.CharField(max_length=500  , blank= False , null = False)

    image = models.ImageField(upload_to = 'questions/tashrihi' , null =True , blank = True)

    exam = models.ForeignKey(Exam , on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('-date' , )
        verbose_name_plural = 'سوالات تشریحی'


    def __str__(self):
        return self.question
    
    

    
class Answer_WQuestion(models.Model):
    
    answer = models.CharField(max_length=500  , null=True , blank = True)
    
    question = models.ForeignKey(Question , on_delete=models.CASCADE , null =False , )
    
    image = models.ImageField(upload_to='answers' , validators=[file_size , ])
    
    student = models.ForeignKey(Student , on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add = True)
    
    
    class Meta:
        verbose_name_plural = 'پاسخ سوالات تشریحی'

    
    def __str__(self):
        return f'answer , {self.answer} , {self.question}'
    


class Answer(models.Model):

    question = models.ForeignKey(Question , on_delete=models.CASCADE , null =False , )
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    selected_choice = models.IntegerField(validators = [validate_ans , ] )
    date = models.DateTimeField(auto_now_add = True)



    class Meta:
        verbose_name_plural = 'پاسخ سوال های تستی'


    
    def __str__(self):
        return type(self).__name__


    


    
    

class TestModel(models.Model):
    name = models.CharField(max_length = 200)
    date_time = models.DateTimeField()
    date = models.DateField()

    def __str__(self):
        return self.name

    
 
