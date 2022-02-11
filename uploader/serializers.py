from rest_framework import serializers
from .models import DropBox
from django.contrib.auth.models import User

class DropBoxSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = DropBox
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'
