from .views import *
from django.urls import path
app_name = 'klass'



urlpatterns = [
   path('<int:pk>' , go_to_class ),
]