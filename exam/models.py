from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

#TODO  : Try pip install django_cleanup , https://stackoverflow.com/questions/16041232/django-delete-filefield
class Question(models.Model):
    
    question = models.CharField(max_length=500  , blank= False , null = False)
    image = models.ImageField(upload_to = '/questions' , null =True , blank = True)
    caution_help = models.CharField(max_length=500  , blank= False , null = False)
    
    class Type_Of_Question(models.Model):
        Four_choices = '4G' , _('4Gozine')
        True_False = 'TF'  , _('True_False')
        Tashrihi = 'TA'  , _('Tashrihi')  
        
    type_of_question = models.CharField(
                                        max_length = 2,
                                        choices=Type_Of_Question.choices,
                                        default=Type_Of_Question.Tashrihi
                                        )
    choiceOne = models.CharField(max_length=500 , null=True , blank = True)
    choiceTwo = models.CharField(max_length=500 , null= True , blank = True)
    choiceThree = models.CharField(max_length=500 , null = True , blank = True)
    choiceFour = models.CharField(max_length=500 , null = True , blank = True)
    
    
 

    