from django.db import models

# Create your models here.

class Video(models.Model):
    
    name = models.CharField(max_length = 300)
    Time_Posted = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='gallery/videos')
    
class Image(models.Model):
    name = models.CharField(max_length = 300)
    Time_Posted = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='gallery/images')

