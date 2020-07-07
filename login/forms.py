from django import forms

class login_Form(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)