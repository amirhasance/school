from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('school_home.urls' , namespace='home')  , name = 'home'),
    path('exam/' , include('exam.urls' , namespace='exam') , name = 'exam'),
    path('class/' , include('klass.urls' , namespace='class') , name = 'class'),
    path('profile/' , include('my_profile.urls', namespace='profile') , name = 'profile')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)