from django.db import models
from datetime import datetime

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length = 400)
   # address = models.CharField(max_length = 400)
   # zip_code = models.IntegerField()

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length = 100)
    Faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    type = models.CharField(max_length = 50)

    def __str__(self):
        return self.type

class Certificate_Type(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Student(models.Model):
    School = models.ForeignKey(School, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 100)
    year_of_graduation = models.IntegerField()
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)
    Grade = models.ForeignKey(Grade, on_delete = models.CASCADE)
    Certificate_Type = models.ForeignKey(Certificate_Type, on_delete = models.CASCADE)

   # first_name = models.CharField(max_length = 40)
   # last_name = models.CharField(max_length = 40)
   # age = models.IntegerField()
   # date_of_resumption = models.DateField(default = datetime.today)

    def __str__(self):
        return self.full_name




