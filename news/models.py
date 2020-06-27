from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):

    title = models.CharField(max_length = 300)
    explanation = models.CharField(max_length = 500)
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news')


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-time',)   
    
def last_3_news():
    return News.objects.all()[:3]


class Comments(models.Model):

    news = models.OneToOneField(News , on_delete=models.CASCADE)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    comment = models.CharField(max_length = 500)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    

