from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class roomName(models.Model):

    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300 , null=True , blank=True)
    is_private = models.BooleanField(default=False)
    time_created = models.TimeField()
    image = models.ImageField(upload_to = 'roomName_images')

    def __str__(self):
        return f'name: {self.name} ,'

class person(User):
    
    image = models.ImageField(upload_to = 'user_images')
    rooms = models.ManyToManyField(roomName )
    
    def __str__(self):
        return f'username {self.username} '

class Message(models.Model):
    author = models.ForeignKey(person , related_name="author_messages" , on_delete=models.CASCADE)
    roomName = models.ForeignKey(roomName , on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'message : {self.content} author : {self.author.username} time : {self.timestamp}'
    
    @staticmethod
    def last_30_messages():
        return Message.objects.order_by('-timestamp').all()[:30]
    
    
    