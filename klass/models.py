from django.db import models
from django.contrib.auth.models import  User 
import os
# Create your models here.

class Teacher(models.Model):
    
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teachers')

    


    def __str__(self):
        return self.user.first_name

    
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)

        super(Teacher, self).delete(*args,**kwargs)
    class Meta:
        verbose_name_plural = "معلمان"
    
    

class Student(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='students')

    class Meta:
        verbose_name_plural = "دانش آموزان"

    
    
    

    def __str__(self):
        return self.user.first_name
    


class Dars(models.Model):
    
    name  = models.CharField(max_length = 200)
    passwd = models.CharField(max_length = 20 , unique=True , blank=False , null = False)
    image = models.ImageField(upload_to='Classes')
    Time_created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher , on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "دروس"

    def __str__(self):
        return self.name


class Tamrin(models.Model):

    name = models.CharField(max_length = 300)

    dars = models.ForeignKey(Dars , on_delete=models.CASCADE)

    file = models.FileField(upload_to=f'tamrin/{dars.name}')

    time_created = models.DateTimeField(auto_now_add=True)

    time_expire = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('time_created',)
        verbose_name_plural = 'تمارین   '
    

                                                 

