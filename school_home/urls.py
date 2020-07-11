from django.urls import path ,include
from . import views
from login.views import log_out

app_name = "shool_home"

urlpatterns = [
    path('' ,views.home , name='home'),
    path('login/' , include('login.urls' , namespace='login') , name='login'),
    path('news/' , include('news.urls' ,namespace='news') , name = 'news'),
    path('ajax/' , views.ajax_comment , name = 'comments'),
    path('logout/' , log_out , name = 'log_out'),
    path('test/' , views.test , name = 'test'),
]


from django.conf import settings
from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)