from django.urls import path
from .views import login , home

app_name = "shool_home"

urlpatterns = [
    path('' , home),
    path('login/' , login )
]