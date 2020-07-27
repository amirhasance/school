
from django.urls import path
from . import views
urlpatterns = [
    path('' , views.teacher_home , name='teacher_home' ),
    path('files/<int:pk>' , views.files , name='files'),
    path('files/create_new/<int:pk>' , views.files_create_new , name='creat-new-file'),
    path('excercise/<int:pk>' , views.excercise , name='exercise'),
    path('excercise/create_new/<int:pk>' , views.excercise_create_new , name= 'excercise_create_new'),
    path('excercise/edit/<int:pk>' , views.excercise_edit , name='excercise_edit'),
]
