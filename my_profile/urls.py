from django.urls import path 
from . import views

app_name = 'my_profile'
urlpatterns = [
    path('my/' , views.my , name = 'my'),

]
