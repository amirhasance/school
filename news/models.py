from django.db import models

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length = 300)
    explanation = models.CharField(max_length = 500)
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news')


    class Meta:
        ordering = ('-time',)
    
def last_3_news():
    return News.objects.all()[:3]

