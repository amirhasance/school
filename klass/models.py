from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(User):
    image = models.ImageField(upload_to='Teachers')
    
    
    
    def __str__(self):
        return 
    
    
    pass


class Student(User):
    image = models.ImageField(upload_to='Students')
    pass


class Dars(models.Model):
    
    name  = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Classes')
    Time_created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    
    pass                                               