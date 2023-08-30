from django.db import models

# Create your models here.#
class SchoolModels(models.Model):
    name = models.CharField(max_length=50,default='')
    number_of_students = models.IntegerField(default = ' ')
    number_of_teachers = models.IntegerField(default = ' ')
    class Meta :
        db_table = 'app1_school'
    

class University(models.Model):
    name = models.CharField(max_length=50,default=' ')
    number_of_students = models.IntegerField(default = 50)
    number_of_teachers = models.IntegerField(default = 5)
    class Meta:
        db_table = 'app1_university'



