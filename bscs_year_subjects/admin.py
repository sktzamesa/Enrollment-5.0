from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import FirstYearSubject
# Register your models here.
@admin.register(FirstYearSubject)
class First_Year_Subject(ModelAdmin):
    list_display = ['Instructors','Subject_code','Subject_name']