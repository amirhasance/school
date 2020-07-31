from .views import create_exam , edit_exam , index , attend
from django.urls import path
app_name = 'exam'



urlpatterns = [
    path('' , index , name = 'index'),
    path('attend/<int:exam_pk>/<int:question_pk>' , attend, name = 'attend'),
    path('create/<int:pk>' , index , name='create_exam'),
    path('edit/<int:pk>' , edit_exam , name='exam_edit'),
]