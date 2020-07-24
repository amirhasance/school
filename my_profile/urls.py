from django.urls import path 
from . import views

app_name = 'my_profile'
urlpatterns = [
    path('my/' , views.my , name = 'my'),
    path('exercise/<int:pk>' , views.exercise , name='exercise'),
    path('my_files/<int:pk>' , views.my_files , name='my_files'),
    path('teacher/'  , views.teacher , name='teacher'),
    path('ajax/' , views.ajax ),

]
