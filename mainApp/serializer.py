from rest_framework import serializers
from . models import *
  
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['user_id','name','email','password','branch']
        