from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Teacher(User):
    image = models.ImageField(upload_to='/Teachers')
    
    
    pass


class Student(User):
    image = models.ImageField(upload_to='/Students')
    pass


class Dars(models.Model):
    name  = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='/Classes')
    Time_created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    
    pass