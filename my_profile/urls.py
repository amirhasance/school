from django.urls import path 
from . import views

app_name = 'my_profile'
urlpatterns = [
    path('my/' , views.my , name = 'my'),
    path('exams/<int:pk>' , views.exams),
    path('form/' , views.form_html , name='form'),
    path('excercise/<int:pk>' , views.exercise , name='exercise'),
    path('my_files/<int:pk>' , views.my_files , name='my_files'),
    path('teacher/'  , views.teacher , name='teacher'),
    path('ajax/' , views.ajax ),

]
