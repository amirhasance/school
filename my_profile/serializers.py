from rest_framework import serializers
from klass.models import Dars , Student 

class Doroos_serializer(serializers.ModelSerializer):
    class Meta :
        model = Dars
        fields = '__all__'
class Student_serializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'
