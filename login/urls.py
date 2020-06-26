from django.urls import path
from .views import login

app_name = 'login'

urlpatterns = [
    path('' , login , name='login')
    # path('student/' , slogin , name = 'studnet_loing'),
    # path('teacher/' , tlogin , name = 'teacher_login'),
]
