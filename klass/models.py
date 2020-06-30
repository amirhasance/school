from django.db import models
from django.contrib.auth.models import  User 
# Create your models here.

class Teacher(models.Model):
    
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teachers')


    def __str__(self):
        return self.user.username
    
    

class Student(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='students')
    
    

    def __str__(self):
        return self.user.username
    


class Dars(models.Model):
    
    name  = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Classes')
    Time_created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
                                                 

