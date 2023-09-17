from rest_framework import serializers 
from .models import SchoolModels,University
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
 
 

class Schoolserializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModels
        fields = ('name','number_of_students','number_of_teachers','user')
    def create(self, validated_data):
        validated_data['user'] = get_object_or_404(User,username=self.context['request'].user)
        return super(SchoolModels,self).create(validated_data)
     


class Universityserializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name','number_of_students','number_of_teachers','user')
    def create(self, validated_data):
        validated_data['user'] = get_object_or_404(User,username=self.context['request'].user)
        return super(University,self).create(validated_data)
     

