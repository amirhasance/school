from django.db import models

from klass.models import Tamrin , Student
from django.core.exceptions import ValidationError
from django.http import HttpResponse
# Create your models here
def file_size(value): # add this to some file where you can import it from
    limit = 1 * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f'حجم فایل  زیاد هست')



class Answer_of_Tamrin_for_every_student(models.Model):

    tamrin =  models.ForeignKey(Tamrin, on_delete=models.CASCADE)

    student = models.ForeignKey(Student, on_delete=models.CASCADE )

    file = models.FileField(upload_to='Tamrin/Answers' , validators=[file_size ])


    def __str__(self):
        return self.tamrin.name
    