from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys



def news_image_size(value):
    limit = 200 * 1024 * 1024 
    if value.size > limit :
        raise ValidationError (f"Image size is Bigger than {limit}")



class Upload(models.Model):
    nameImage = models.CharField(max_length = 140,blank=False,null=True)
    uploadedImage =  models.ImageField(upload_to = 'Upload/',blank=False,null=True)
    def save(self, *args, **kwargs):
        if not self.id:
            self.uploadedImage = self.compressImage(self.uploadedImage)
        super(Upload, self).save(*args, **kwargs)
    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=10)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage
    


class News(models.Model):

    title = models.CharField(max_length = 300)
    explanation = models.TextField()
    time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news'  , validators=[news_image_size])

    def save(self , *args , **kwargs):
        if not self.id :
            self.image = self.compressImage(self.image)
        super(News , self).save(*args , **kwargs)
    
    def compressImage(self , image) :
        imageTemproary = Image.open(image)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=10)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image

       


    def __str__(self):
        return self.title
    
    def summery(self):
        return self.explanation[:60]

    def is_long(self):
        return len(self.explanation)>60
    
    
    class Meta:
        ordering = ('-time',)   
        verbose_name_plural = "اخبار مدرسه"
    

    
def last_3_news():
    return News.objects.all()[:6]


class Comments(models.Model):

    news = models.ForeignKey(News , on_delete=models.CASCADE)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    comment = models.CharField(max_length = 500)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    


