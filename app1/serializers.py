from rest_framework import serializers 
from .models import SchoolModels,University
 

class Schoolserializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModels
        fields = ('name','number_of_students','number_of_teachers')

class Universityserializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name','number_of_students','number_of_teachers')

