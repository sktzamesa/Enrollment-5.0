from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearFirstSemesterInstructor
# Register your models here.
@admin.register(FirstYearFirstSemesterInstructor)
class InstructorAdmin(ModelAdmin):
    list_display = ['First_name']

