from django.forms import ModelForm
from .models import Answer_of_Tamrin_for_every_student
from django import forms

class Tamrin_Form(forms.ModelForm):
    class Meta:
        model = Answer_of_Tamrin_for_every_student
        fields = '__all__'
    
    