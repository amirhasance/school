from django.contrib import admin

# Register your models here.
from .models import Message , person , roomName
admin.site.register(roomName)
admin.site.register(Message)
admin.site.register(person)