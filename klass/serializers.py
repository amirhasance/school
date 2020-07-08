from rest_framework import serializers
from .models import Dars , Tamrin

class Dars_serializer(serializers.ModelSerializer):
    class Meta:
        model = Dars
        fields = ('__all__'  )

class Tamrin_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tamrin
        fields = ('__all__')

