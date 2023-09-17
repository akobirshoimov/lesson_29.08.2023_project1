from django.db import models
from django.contrib.auth.models import User

# Create your models here.#
class SchoolModels(models.Model):
    name = models.CharField(max_length=50,default='')
    number_of_students = models.IntegerField(default = ' ')
    number_of_teachers = models.IntegerField(default = ' ')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # class Meta :
    #     db_table = 'app1_school'
    # def __str__(self) -> str:
    #     return self.name
    

class University(models.Model):
    name = models.CharField(max_length=50,default=' ')
    number_of_students = models.IntegerField(default = 50)
    number_of_teachers = models.IntegerField(default = 5)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # class Meta:
    #     db_table = 'app1_university'
    # def __str__(self) -> str:
    #     return self.name