from django.contrib import admin 

from .models import Student,Teacher,Contractor
# Register your models here.

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','date','age','fees']

@admin.register(Teacher)

class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','date','age','salary']

@admin.register(Contractor)

class ContractorAdmin(admin.ModelAdmin):
    list_display=['id','name','date','age','payment']

