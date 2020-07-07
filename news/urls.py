from django.urls import path , include
from . import views

app_name = 'news'

urlpatterns = [
    path('' , views.site_news , name ='site_news'),
    path('<int:pk>' , views.this_new , name='this_new')
]
