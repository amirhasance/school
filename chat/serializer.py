from .models import person , Message , roomName
from rest_framework import serializers

class person_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = person
        fields = ['image' , 'username' , 'password']

class Message_serializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Message
        fields = '__all__'

class Room_serializer (serializers.ModelSerializer):
    class Meta:
        model = roomName    
        fields = '__all__'