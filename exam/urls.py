from .views import create_exam , edit_exam , index
from django.urls import path
app_name = 'exam'



urlpatterns = [
    path('' , index , name = 'index'),
    path('create/' , create_exam  , name='create_exam'),
    path('edit/<int:pk>' , edit_exam , name='exam_edit'),
]