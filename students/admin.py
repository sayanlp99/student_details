from django.contrib import admin
from .models import *
from .forms import StudentForm

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    list_display = ["name", "email", "dob", "gender"]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["department"]