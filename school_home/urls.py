from django.urls import path ,include
from .views import   home

app_name = "shool_home"

urlpatterns = [
    path('' , home , name='home'),
    path('login/' , include('login.urls' , namespace='login') , name='login'),
    path('news/' , include('news.urls' ,namespace='news') , name = 'news'),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)