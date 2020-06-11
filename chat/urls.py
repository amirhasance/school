
from django.urls import path , re_path
from  .views import index ,room , test , login  , signin

app_name = 'chat'

urlpatterns = [
    
    path('test/' , test , name='test'),
    path('login/' , login , name='login'),
    path('signin/' , signin , name='signin'),

    path('' , index , name='index'),
    #  path('<str:room_name>/', views.room, name='room'),
    re_path(r'^(?P<room_name>[^/]+)/$' , room , name='room')
    
    
    
]
