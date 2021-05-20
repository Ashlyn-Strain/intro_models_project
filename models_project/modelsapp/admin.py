from django.contrib import admin
from .models import Student, School, Faculty, Grade, Certificate_Type, Department

# Register your models here.

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Grade)
admin.site.register(Certificate_Type)
admin.site.register(Department)
