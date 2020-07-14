from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('' , views.site_login , name='login'),
    path('logout/' , views.site_logout , name = 'logout'),
    path('teacher/' , views.tlogin , name = 'teacher_login')
    # path('student/' , slogin , name = 'studnet_loing'),
    # path('teacher/' , tlogin , name = 'teacher_login'),
]
