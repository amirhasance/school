from django.urls import path
from . import views

app_name = "shool_home"

urlpatterns = [
    path('' , views.home)
]